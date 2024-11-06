import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

user = input('What is your name?')
print('What would you like to send?')
mess = ''
while True:
    message = input()
    if message == ' ':
        break
    message += '\n'
    mess += message
final_message = ('{}\n\nSent by: @{}'.format(mess, user))

client.chat_postMessage(channel='#general', text=final_message)