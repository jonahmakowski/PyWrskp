current_time = input()
class_ends = input()

# Parse hours and minutes from input strings
current_hour, current_minute = map(int, current_time.split(':'))
class_end_hour, class_end_minute = map(int, class_ends.split(':'))

# Calculate time difference in minutes
if class_end_hour > current_hour or (class_end_hour == current_hour and class_end_minute >= current_minute):
    # Class ends on the same day
    time_difference = (class_end_hour - current_hour) * 60 + (class_end_minute - current_minute)
else:
    # Class ends on the next day
    time_difference = (class_end_hour + 24 - current_hour) * 60 + (class_end_minute - current_minute)

print(time_difference)
