from helper import *
import os
import time
import random
# random.choice(lis)


class Main:
    def __init__(self):
        os.system('clear')
        logging('System Bootup')
        self.login_check = False
        self.security_clearence = 0
        self.username = ''
        self.name = ''
        self.password = ''
        self.login_checker(first=True)

    def hub(self):
        self.login_checker()
        while True:
            print('Options are:')
            print('\t- messanger send')
            print('\t- messanger read')
            print('\t- view passwords')
            print('\t- music')
            print('\t- logout')
            print('\t- encrypt')
            print('\t- decrypt')
            print('\t- view log')
            option = input('What would you like to do?\n')
            if option == 'messanger send':
                self.messanger_send()
            elif option == 'messanger read':
                self.messager_read()
            elif option == 'view passwords':
                self.view_passwords()
            elif option == 'music':
                self.music()
            elif option == 'logout':
                print('Warning!')
                print('The safest way to logout is to end and restart the program.')
                time.sleep(2)
                self.__init__()
            elif option == 'encrypt':
                self.encrypt()
            elif option == 'decrypt':
                self.decrypt()
            elif option == 'view log':
                self.view_log()
            else:
                print('{} is not an option!'.format(option))
            time.sleep(2)
            self.clear()

    def original_login(self):
        logging('User Login Attempt')
        info = decrypt_txt()
        user = input('input your username\n')
        password = input('input you password\n')
        for item in info:
            if item['user'] == user and item['password'] == password:
                print('successfully logged in!')
                self.login_check = True
                self.security_clearence = int(item['clearance'])
                self.username = item['user']
                self.password = item['password']
                logging('User successfully logged in')
                time.sleep(2)
                self.clear()
        if not self.login_check:
            logging('User Failed To Login With Username {} and password {}'.format(user, password))
            print('login fail!')

    def other_login(self):
        logging('Other Login has been activated')
        user = input('input your username\n')
        password = input('input you password\n')
        if user == self.username and password == self.password:
            logging('User successfully Other Logged in')
            self.clear()
            return True
        else:
            logging('User Failed To Other Login With Username {} and password {}'.format(user, password))
            self.clear()
            return False

    def messanger_send(self, message=None, encrypt=None, key=None):
        logging('User is sending a message')
        e = Encrption()
        self.login_checker()
        if message is None:
            message = input('What is the message you would like to send?\n')
        if encrypt is None:
            while True:
                encrypt = input('Would you like to encrypt the message? (y/n)\n')
                if encrypt == 'y' or encrypt == 'n':
                    break
                print('That is not y or n')
                print('Try again')
        if encrypt == 'y':
            if key is None:
                while True:
                    try:
                        key = int(input('What would you like the key to be? (This must be a number)\n'))
                        break
                    except ValueError:
                        print('That is not a number!')
                        print('Try again')
            message = e.encrypt(message, key)
        write_file('message.txt', message)
        print('Your message was saved at message.txt!')
        time.sleep(2)
        self.clear()

    def messager_read(self, encrypt=None, key=None):
        logging('User is reading a message')
        e = Encrption()
        self.login_checker()
        if encrypt is None:
            while True:
                encrypt = input('Is the message encrypted? (y/n)\n')
                if encrypt == 'y' or encrypt == 'n':
                    break
                print('That is not y or n')
                print('Try again')
        if encrypt == 'y':
            if key is None:
                while True:
                    try:
                        key = int(input('What is the key? (This must be a number)\n'))
                        break
                    except ValueError:
                        print('That is not a number!')
                        print('Try again')

        message = read_file('message.txt')
        if encrypt == 'y':
            message = e.decrypt(message, key)
        print('Your message is {}'.format(message))
        input('Press enter after reading to clear')
        self.clear()

    def clearance_check(self, clearance):
        self.login_checker()
        print('To access this program you must log in again!')
        if not self.other_login():
            print('Login Usuccesfull!')
            return 'Login Fail'
        if self.security_clearence >= clearance:
            return True
        else:
            return False

    def view_passwords(self):
        if not self.clearance_check(100):
            print("You don't have the needed clearance level (100), to preform this action")
            return
        info = decrypt_txt()
        direct = read_file('txt.txt')
        print('User\t\tPassword\tName\tClearance\tKey')
        count = 0
        logging('User {} is viewing the passwords'.format(self.username))
        for item in info:
            print('{}\t{}\t\t{}\t{}\t\t{}'.format(item['user'],
                                              item['password'],
                                              item['name'],
                                              item['clearance'],
                                              direct[count]['key']))
            count += 1
        print()
        print()
        input('Press Enter To Complete Viewing Session\nSession Will End Two Seconds After Your Press Enter')
        return

    def music(self):
        while True:
            if not self.login_check:
                print('Not logged in')
                self.original_login()
            else:
                break
        play_music()

    def login_checker(self, first=False):
        if first:
            self.original_login()
        while True:
            if not self.login_check:
                print('You have not yet logged in')
                self.original_login()
            elif self.login_check:
                break

    @staticmethod
    def clear():
        os.system('clear')

    def decrypt(self):
        self.login_checker()
        e = Encrption()
        message = input('What is the message?\n')
        while True:
            try:
                key = int(input('What is the key? (This must be a number)\n'))
                break
            except ValueError:
                print('That is not a number!')
                print('Try again')
        print('Your message is {}'.format(e.decrypt(message, key)))

    def encrypt(self):
        self.login_checker()
        e = Encrption()
        message = input('What is the message?\n')
        while True:
            try:
                key = int(input('What is the key? (This must be a number)\n'))
                break
            except ValueError:
                print('That is not a number!')
                print('Try again')
        print('Your encoded message is:')
        print(e.encrypt(message, key))

    def view_log(self):
        if not self.clearance_check(50):
            print("You don't have the needed clearance level (50), to preform this action")
            return
        logging('user {} is viewing logs!'.format(self.username))
        logs = read_file('log.txt')
        print('Info, Datetime')
        for item in logs:
            print('{}, {}'.format(item['log'], item['datetime']))
        input('\n\nPress enter to go back to hub!')
        return

    def math_test(self):
        self.login_checker()
        score = 0
        print('Welcome {}!'.format(self.username))
        print('This is a math test with randomly generated awnsers and questions!')
        print('Warning, some questions may result in a negitive ' +
              'or a decimal, and a decimal or negetive will be expected')
        time.sleep(2)
        while True:
            self.clear()
            num1 = random.randint(-1000, 1000)
            num2 = random.randint(-1000, 1000)
            operation = random.randint(1,4)
            if operation == 1:
                question = ('What is {} + {}?'.format(num1, num2))
                awnser = num1 + num2
            elif operation == 2:
                question = ('What is {} - {}?'.format(num1, num2))
                awnser = num1 - num2
            elif operation == 3:
                question = ('What is {} * {}?'.format(num1, num2))
                awnser = num1 * num2
            else:
                question = ('What is {} / {}?'.format(num1, num2))
                awnser = num1 / num2
            while True:
                print(question)
                user_input = input()
                if user_input == '':
                    return
                try:
                    user_input = float(user_input)
                except ValueError:
                    print('That is not a number, try again')

m = Main()
m.hub()
