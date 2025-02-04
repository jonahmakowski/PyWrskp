from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import datetime as dt, timedelta
import pytz
import math
from api_access import get_credentials

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('calendar', 'v3', credentials=creds)

def split_into_chunks(total_duration, min_chunk, max_chunk):
    if total_duration < 0 or min_chunk <= 0 or max_chunk <= 0:
        raise ValueError("Invalid input values")
    if min_chunk > max_chunk:
        raise ValueError("Minimum chunk must be <= maximum chunk")
    if total_duration == 0:
        return []
    if min_chunk <= total_duration <= max_chunk:
        return [total_duration]
    
    k_min = math.ceil(total_duration / max_chunk)
    min_total = k_min * min_chunk
    if min_total > total_duration:
        raise ValueError(f"Cannot split {total_duration}h with given chunk constraints")
    
    remaining = total_duration - min_total
    max_extra = max_chunk - min_chunk
    if remaining > k_min * max_extra:
        raise ValueError("Cannot split with current constraints")
    
    num_full_extra = remaining // max_extra
    partial_extra = remaining % max_extra
    chunks = [max_chunk] * num_full_extra
    if partial_extra:
        chunks.append(min_chunk + partial_extra)
    chunks += [min_chunk] * (k_min - len(chunks))
    chunks.sort(reverse=True)
    return chunks

def main():
    service = get_calendar_service()
    calendar = service.calendars().get(calendarId='primary').execute()
    tz_str = calendar.get('timeZone', 'UTC')
    tz = pytz.timezone(tz_str)

    task_name = input("Enter task name: ")
    total_duration = float(input("Total duration needed (hours): "))
    due_date_str = input("Due date (YYYY-MM-DD HH:MM): ")
    due_date = tz.localize(dt.strptime(due_date_str, "%Y-%m-%d %H:%M"))
    min_chunk = float(input("Minimum session duration (hours): "))
    max_chunk = float(input("Maximum session duration (hours): "))

    try:
        chunks = split_into_chunks(total_duration, min_chunk, max_chunk)
        print(f"Scheduled sessions: {chunks}")
    except ValueError as e:
        print(e)
        return

    now = dt.now(tz)
    if due_date < now:
        print("Due date must be in the future")
        return

    events_result = service.events().list(
        calendarId='primary',
        timeMin=now.isoformat(),
        timeMax=due_date.isoformat(),
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    
    busy_events = []
    for event in events_result.get('items', []):
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        if 'T' in start:
            start_dt = dt.fromisoformat(start).astimezone(tz)
            end_dt = dt.fromisoformat(end).astimezone(tz)
        else:
            start_dt = tz.localize(dt.combine(dt.fromisoformat(start).date(), dt.min.time()))
            end_dt = tz.localize(dt.combine(dt.fromisoformat(end).date(), dt.min.time()))
        busy_events.append({'start': start_dt, 'end': end_dt})

    def merge_events(events):
        if not events: return []
        sorted_events = sorted(events, key=lambda x: x['start'])
        merged = [sorted_events[0]]
        for event in sorted_events[1:]:
            last = merged[-1]
            if event['start'] <= last['end']:
                merged[-1]['end'] = max(last['end'], event['end'])
            else:
                merged.append(event)
        return merged

    free_slots = []
    current_start = now
    for event in merge_events(busy_events):
        if event['start'] > current_start:
            free_slots.append((current_start, event['start']))
        current_start = max(current_start, event['end'])
    if current_start < due_date:
        free_slots.append((current_start, due_date))

    events_to_create = []
    for chunk in chunks:
        chunk_duration = timedelta(hours=chunk)
        scheduled = False
        for i in range(len(free_slots)):
            slot_start, slot_end = free_slots[i]
            if (slot_end - slot_start) >= chunk_duration:
                event_end = slot_start + chunk_duration
                events_to_create.append((slot_start, event_end))
                if event_end < slot_end:
                    free_slots[i] = (event_end, slot_end)
                else:
                    del free_slots[i]
                scheduled = True
                break
        if not scheduled:
            print("Couldn't schedule all sessions")
            return

    for start, end in events_to_create:
        event = {
            'summary': task_name,
            'start': {'dateTime': start.isoformat(), 'timeZone': tz_str},
            'end': {'dateTime': end.isoformat(), 'timeZone': tz_str},
        }
        service.events().insert(calendarId='primary', body=event).execute()
        print(f"Scheduled: {start.strftime('%Y-%m-%d %H:%M')} to {end.strftime('%H:%M')}")

if __name__ == '__main__':
    get_credentials()
    main()