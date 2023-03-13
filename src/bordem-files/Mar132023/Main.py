import time
import random
import json
from helper import *
# random.choice(lis)


class Main:
    def __init__(self):
        self.login_check = False
        self.security_clearence = 0
        self.username = ''
        self.name = ''
        self.login()

    def login(self):
        info = decrypt_txt()
        user = input('input your username\n')
        password = input('input you password\n')
        for item in info:
            if item['user'] == user and item['password'] == password:
                print('successfully logged in!')
                self.login_check = True
                self.security_clearence = item['clearance']
                self.username = item['user']
        if not self.login_check:
            exit()


m = Main()
