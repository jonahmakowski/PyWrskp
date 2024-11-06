import re
from datetime import datetime

def convert_date_format(match):
    date_str = match.group(0)
    date_obj = datetime.strptime(date_str, '%d %b %Y')
    new_date_str = date_obj.strftime('#%Y-%m-%d')
    return new_date_str

def replace_dates_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regular expression to find dates in the format D MMM YYYY
    date_pattern = re.compile(r'\b(\d{1,2} [A-Z][a-z]{2} \d{4})\b')
    new_content = date_pattern.sub(convert_date_format, content)

    with open(file_path, 'w') as file:
        file.write(new_content)

# Example usage
file_path = 'Swimming Archive.md'  # Replace with your file path
replace_dates_in_file(file_path)