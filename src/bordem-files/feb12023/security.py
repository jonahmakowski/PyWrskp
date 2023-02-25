import time
import random

class Security:
    def __init__(self):
        self.attempts = []
        self.username = None
        self.password = None

    def get_info(self, username, password):
        self.username = username
        self.password = password
        self.attempts.append('get_info')

    def test(self, item, error):
        temp = False
        for item in self.attempts:
            if item == item:
                temp = True
        if temp != True:
            for i in range(50):
                print('ERROR, {}'.format(error))
            return('error')
        else:
            return('accepted')

    def login(self):
        if self.test('get_info', 'attempted login failed, no info detected!') == 'error':
            exit()
        else:
            print('authenticating username and password')
            time.sleep(random.randint(1,5))
            if self.username == 'WhiteSwine' and self.password == 'bored':
                print('authanticated')
                self.attempts.append('login')
                return

s = Security()
s.get_info(input('What is your username? \n'), input('What is your password? \n'))
s.login()