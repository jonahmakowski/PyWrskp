from helper import *
# random.choice(lis)


class Main:
    def __init__(self):
        logging('System Bootup')
        self.login_check = False
        self.security_clearence = 0
        self.username = ''
        self.name = ''
        self.password = ''
        self.original_login()

    def hub(self):
        while True:
            if not self.login_check:
                print('You are not logged in')
                self.original_login()
            else:
                break
        while True:
            option = input('What would you like to do?\n')
            if option == 'messanger send':
                self.messanger_send()
            elif option == 'messanger read':
                self.messager_read()
            elif option == 'view passwords':
                self.view_passwords()
            else:
                print('{} is not an option!'.format(option))
            print()
            print()
            print()
            print()
            print()
            print()

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
        if not self.login_check:
            logging('User Failed To Login With Username {} and password {}'.format(user, password))
            print('login fail!')

    def other_login(self):
        logging('Other Login has been activated')
        user = input('input your username\n')
        password = input('input you password\n')
        if user == self.username and password == self.password:
            logging('User successfully Other Logged in')
            return True
        else:
            logging('User Failed To Other Login With Username {} and password {}'.format(user, password))
            return False

    def messanger_send(self, message=None, encrypt=None, key=None):
        logging('User is sending a message')
        e = Encrption()
        if not self.login_check:
            print('Error, you have not yet been logged in!')
            print('rederecting you to login!')
            self.login()
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

    def messager_read(self, encrypt=None, key=None):
        logging('User is reading a message')
        e = Encrption()
        if not self.login_check:
            print('Error, you have not yet been logged in!')
            print('rederecting you to login!')
            self.login()
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

    def clearance_check(self, clearance):
        if not self.login_check:
            print('You have not yet logged in')
            self.original_login()
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


m = Main()
m.hub()
