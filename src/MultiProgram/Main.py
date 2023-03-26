from helper import *
import os
import time
import random
import turtle
import threading
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
            print('\t- math game')
            print('\t- lowest common multiple')
            print('\t- add user')
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
            elif option == 'math game':
                self.math_game()
            elif option == 'lowest common multiple':
                self.lowest_common_multiple()
            elif option == 'add user':\
                self.add_user()
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
                self.name = item['name']
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
                key = number_input('What would you like the key to be? (This must be a number)\n')
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
                key = number_input('What is the key? (This must be a number)\n')

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
            return False
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
        key = number_input('What is the key? (This must be a number)\n')
        print('Your message is {}'.format(e.decrypt(message, key)))

    def encrypt(self):
        self.login_checker()
        e = Encrption()
        message = input('What is the message?\n')
        key = number_input('What is the key? (This must be a number)\n')
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

    def math_game(self):
        self.login_checker()
        score = 0
        print('Welcome {}!'.format(self.username))
        print('This is a math test with randomly generated awnsers and questions!')
        print('Warning, some questions may result in a negitive ' +
              'or a decimal, and a decimal or negetive will be expected')
        logging('User is playing a math game')
        max_score = read_file('math.txt')
        if max_score != []:
            print('The current high score is {}'.format(max_score))
        time.sleep(2)
        countinue = True
        while countinue:
            self.clear()
            num1 = random.randint(-10, 10000)
            num2 = random.randint(-10, 10000)
            operation = random.randint(1, 4)
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
                user_input = input('If you now longer wish to play, press enter without a number or space\n')
                if user_input == '':
                    countinue = False
                    break
                try:
                    user_input = float(user_input)
                    break
                except ValueError:
                    print('That is not a number, try again')
            if countinue:
                if user_input == awnser:
                    print('Good Job, that is correct')
                    score += 1
                    print('Your current score is {}'.format(score))
                    if score == max_score:
                        print('Good Job, you have hit the max score!')
                    elif score < max_score:
                        print('You still have {} to go before you hit the max score'.format(max_score - score))
                    elif score > max_score:
                        print('You are {} over the current top score'.format(score - max_score))
                else:
                    print('Bad Job, that is incorrect')
                    print('The correct awnser is {}, and yours was {}'.format(awnser, user_input))
                    print('Your current score is {}'.format(score))
                input('Press Enter to Countinue!')
        max_score = read_file('math.txt')
        if score > max_score:
            print('You beat the current max score by {}'.format(score - max_score))
            write_file('math.txt', score)
            logging('Player {} beat the max score (of {}) and set a new max score as {}'.format(self.username,
                                                                                                max_score,
                                                                                                score))

    def lowest_common_multiple(self):
        self.login_checker()
        numb = number_input('The first number you want to check')
        numb2 = number_input('The second number you want to check')
        ma = number_input('Max amount of loops (Greater the number, greater the time.)')
        result = check_lowest_common_multiple(numb, numb2, ma)
        if result is False:
            print('The program could not find a result in the max of {} you gave.'.format(ma))
        else:
            print('The lowest common multiple between {} and {} is {}'.format(numb, numb2, result))

    def add_user(self):
        self.login_checker()
        if not self.clearance_check(100):
            print("You don't have high enough clearnance (100)")
            return
        username = input("Enter the new user's username\n")
        password = input("Enter the new user's password\n")
        clearance = input("Enter the new user's clearance\n")
        name = input("What is the new user's name?\n")
        key = number_input("Enter the new user's encryption key")
        e = Encrption()
        name = e.encrypt(name, key)
        username = e.encrypt(username, key)
        password = e.encrypt(password, key)
        clearance = e.encrypt(clearance, key)
        username_name = e.encrypt('user', key)
        password_name = e.encrypt('password', key)
        clearance_name = e.encrypt('clearance', key)
        name_name = e.encrypt('name', key)
        current_users = read_file('txt.txt')
        current_users.append({username_name: username,
                              password_name: password,
                              clearance_name: clearance,
                              'key': key,
                              name_name: name})
        write_file('txt.txt', current_users)


m = Main()
m.hub()
