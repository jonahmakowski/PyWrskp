import time
import datetime
import json
import sys
sys.path.append('../../coder-decoder')
import coder # my program that can code and encode text

class Phone:
    def __init__(self):
        self.log = {}
        self.fetch_log() # gets info from the log
        self.password = self.log['password']
        self.username = self.log['username']
        self.name = self.log['name']
        self.login() # asks for password
        self.do() # asks what you want to do
    
    def login(self):
        passtest = input('What is your phone password?')
        print('Checking passwords,')
        time.sleep(1)
        print('Looking for hacks,')
        time.sleep(1)
        if passtest == self.password:
            return
        else:
            print('That password is incorrect')
            time.sleep(10)
            exit()
    
    def do(self):
        print('Welcome Back, {} ({})'.format(self.username, self.name))
        now = datetime.datetime.now()
        self.log['loginDate'].append(str(now))
        self.push_log()
        option = input('What would you like to do?')
        option = option.lower()
        if option == 'send uncoded message' or option == 'sum':
             self.send_uncoded_message()
        elif option == 'send coded message' or option == 'scm':
            self.send_coded_message()
        elif option == 'tell noah to kick his butt' or option == 'tntkhb':
            self.tell_noah_to_kick_his_butt()
         
    def fetch_log(self):
        with open('../../../docs/txt-files/phone_log.txt') as json_file:
                self.log = json.load(json_file)
    
    def push_log(self):
        with open('../../../docs/txt-files/phone_log.txt', 'w') as outfile:
            json.dump(self.log, outfile)
    
    def send_uncoded_message(self, message=None, location=None):
        now = str(datetime.datetime.now())
        coded = True
        if message == None and location == None:
            message = input('What is your message?')
            coded = False
        location = input('What is the location or name?')
        location = '{}.txt'.format(location)
            
        try:
            with open(location, 'w') as outfile:
                json.dump(message, outfile)
            self.log['messages'].append({'Date': now, 'message': message, 'location_created_at': location, 'coded': coded})
            self.push_log()
        except:
            print('{} is not a valid location'.format('location'))
    
    def send_coded_message(self):
        cod = coder.CoderDecoder(print_info=False)
        key = int(input('What is the shift number you would like?\n'))
        message = input('What is the message you would like to send?\n')
        cod.add_vars(message, key)
        coded_message = cod.code()
        self.send_uncoded_message(message=coded_message)
    
    def tell_noah_to_kick_his_butt(self):
        print('Noah, {} has told you to kick your butt!'.format(self.username))

Jphone = Phone()
