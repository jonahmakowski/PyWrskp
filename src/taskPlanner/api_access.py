import datetime
import os.path
from dateutil.parser import parse as date_parser

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_credentials():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def get_events(amount):
  creds = get_credentials()
  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()  # 'Z' indicates UTC time
    print("Getting the upcoming {} events".format(amount))
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=amount,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return


    print(events[0])
    # Prints the start and name of the next 10 events
    output = []
    for index, event in enumerate(events):
      start = date_parser(event["start"].get("dateTime", event["start"].get("date")))
      end = date_parser(event["end"].get("dateTime", event["start"].get("date")))
      location = event['location'].replace('\n', ' ') if 'location' in event.keys() else None
      title = event['summary']
      output.append({'title': title, 'location': location, 'start': start, 'end': end})
      print(f"{index + 1}.\t{start.strftime('%d/%m/%Y, %H:%M')} - {end.strftime('%d/%m/%Y, %H:%M')} -- {title} at {location}")
    
    return output

  except HttpError as error:
    print(f"An error occurred: {error}")
    return False

def make_event(start, end, title):
    creds = get_credentials()
    service = build("calendar", "v3", credentials=creds)
    service.events().insert(calendarId='primary', body={
        'summary': title,
        'start': {
            'dateTime': start,
            'timeZone': 'America/Toronto'
        },
        'end': {
            'dateTime': end,
            'timeZone': 'America/Toronto'
        }
    }).execute()

if __name__ == "__main__":
  events = get_events(200)
  make_event('2025-01-01T10:00:00', '2025-01-01T11:00:00', 'Test event')