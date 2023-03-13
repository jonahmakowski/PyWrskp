from helper import *
# random.choice(lis)


class Main:
    def __init__(self):
        logging('System Bootup')
        self.login_check = False
        self.security_clearence = 0
        self.username = ''
        self.name = ''
        self.login()

    def login(self):
        logging('User Login Attempt')
        info = decrypt_txt()
        user = input('input your username\n')
        password = input('input you password\n')
        for item in info:
            if item['user'] == user and item['password'] == password:
                print('successfully logged in!')
                self.login_check = True
                self.security_clearence = item['clearance']
                self.username = item['user']
                logging('User successfully logged in')
        if not self.login_check:
            logging('User Failed To Login With Username {} and password {}'.format(user, password))
            print('login fail!')

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


m = Main()
