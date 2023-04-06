import time
import random
import pyWrskp
from helper import *


class Main:
    def __init__(self):
        clear()
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
            option = question_window('Options are:\n' +
                                     '\t- messanger send\n' +
                                     '\t- messanger read\n' +
                                     '\t- view passwords\n' +
                                     '\t- music\n' +
                                     '\t- logout\n' +
                                     '\t- encrypt\n' +
                                     '\t- decrypt\n' +
                                     '\t- view log\n' +
                                     '\t- math game\n' +
                                     '\t- lowest common multiple\n' +
                                     '\t- add user\n' +
                                     '\t- mastermind\n' +
                                     '\n\n\nWhat would you like to do?',
                                     'Hub')
            if option == 'messanger send':
                self.messanger_send()
            elif option == 'messanger read':
                self.messager_read()
            elif option == 'view passwords':
                self.view_passwords()
            elif option == 'music':
                self.music()
            elif option == 'logout' or option is None:
                show_window('Warning!\n' +
                            'The safest way to logout is to end and restart the program.\n'
                            'Press OK to continue',
                            'logout')
                self.__init__()
            elif option == 'encrypt':
                self.encrypt_local()
            elif option == 'decrypt':
                self.decrypt_local()
            elif option == 'view log':
                self.view_log()
            elif option == 'math game':
                self.math_game()
            elif option == 'lowest common multiple':
                self.lowest_common_multiple()
            elif option == 'add user':
                self.add_user()
            elif option == 'mastermind':
                self.mastermind()
            else:
                show_window('{} is not an option!'.format(option),
                            'Hub Error')
            time.sleep(2)
            clear()

    def original_login(self):
        logging('User Login Attempt')
        info = decrypt_txt()
        user = question_window('input your username', 'Login Username')
        password = question_window('input you password', 'Login Password')
        for item in info:
            if item['user'] == user and item['password'] == password:
                show_window('successfully logged in!', 'Successfull Login!')
                self.login_check = True
                self.security_clearence = int(item['clearance'])
                self.username = item['user']
                self.password = item['password']
                self.name = item['name']
                logging('User successfully logged in')
                clear()
        if not self.login_check:
            logging('User Failed To Login With Username {} and password {}'.format(user, password))
            show_window('login fail!', 'Failed Login!')

    def other_login(self):
        logging('Other Login has been activated')
        user = question_window('input your username', 'Login Username')
        password = question_window('input you password', 'Login Password')
        if user == self.username and password == self.password:
            logging('User successfully Other Logged in')
            clear()
            return True
        else:
            logging('User Failed To Other Login With Username {} and password {}'.format(user, password))
            clear()
            return False

    def messanger_send(self, message=None, encrypt=None, key=None):
        logging('User is sending a message')
        self.login_checker()
        if message is None:
            message = question_window('What is the message you would like to send?', 'Message Send')
        if encrypt is None:
            while True:
                encrypt = question_window('Would you like to encrypt the message? (y/n)', 'Message Encryption?')
                encrypt = encrypt.lower()
                if encrypt == 'y' or encrypt == 'n':
                    break
                show_window('That is not y or n' +
                            'Try again',
                            'not y or n')
        if encrypt == 'y':
            if key is None:
                key = number_input_local('What would you like the key to be?')
            message = pyWrskp.encrypt(key, message)
        write_file('message.txt', message)
        show_window('Your message was saved at message.txt!', 'Successfull Message Save')
        time.sleep(2)
        clear()

    def messager_read(self, encrypt=None, key=None):
        logging('User is reading a message')
        self.login_checker()
        if encrypt is None:
            while True:
                encrypt = question_window('Is the message encrypted? (y/n)', 'Message Encryption?')
                encrypt = encrypt.lower()
                if encrypt == 'y' or encrypt == 'n':
                    break
                show_window('That is not y or n' +
                            'Try again',
                            'not y or n')
        if encrypt == 'y':
            if key is None:
                key = number_input_local('What is the key? (This must be a number)\n')

        message = read_file('message.txt')
        if encrypt == 'y':
            message = decrypt(key, message)
        show_window('Your message is {}!'.format(message),
                    'Message Result')
        clear()

    def clearance_check(self, clearance):
        show_window('To access this program you must log in again!',
                    'Re-Login Needed')
        if not self.other_login():
            show_window('Login Usuccesfull!',
                        'Failed Login')
            return False
        if self.security_clearence >= clearance:
            return True
        else:
            return False

    def view_passwords(self):
        self.login_checker()
        if not self.clearance_check(100):
            show_window("You don't have the needed clearance level (100), to preform this action",
                        'Not Enough Clearance')
            return
        info = decrypt_txt()
        direct = read_file('txt.txt')
        print('User, Password, Name, Clearance, Key')     # TODO transfer lines to psg
        count = 0
        logging('User {} is viewing the passwords'.format(self.username))
        for item in info:
            print('{}, {}, {}, {}, {}'.format(item['user'],
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
        self.login_checker()
        play_music()

    def login_checker(self, first=False):
        if first:
            self.original_login()
        while True:
            if not self.login_check:
                show_window('You have not yet logged in', 'Not Logged in')
                self.original_login()
            elif self.login_check:
                break

    def decrypt_local(self):
        self.login_checker()
        message = question_window('What is the message?\n', 'Message')
        key = number_input_local('What is the key?')
        show_window('Your message is {}'.format(decrypt(key, message)), 'Message')

    def encrypt_local(self):
        self.login_checker()
        message = question_window('What is the message?\n', 'Message')
        key = number_input_local('What is the key')
        show_window('Your encoded message is:\n' +
                    pyWrskp.encrypt(key, message),
                    'Message')

    def view_log(self):
        self.login_checker()
        if not self.clearance_check(50):
            show_window("You don't have the needed clearance level (50), to preform this action",
                        'Not enough clearance')
            return
        logging('user {} is viewing logs!'.format(self.username))
        logs = read_log()
        display_logs(list(reversed(logs)))
        input('\n\nPress enter to go back to hub!')
        return

    def math_game(self):
        self.login_checker()
        score = 0
        show_window('Welcome {}!\n'.format(self.username) +
                    'This is a math test with randomly generated awnsers and questions!\n' +
                    'Warning, some questions may result in a negitive ' +
                    'or a decimal, and a decimal or negetive will be expected',
                    'Math Game Rules')
        logging('User is playing a math game')
        max_score = read_file('math.txt')
        if max_score != []:
            show_window('The current high score is {}'.format(max_score),
                        'High Score')
        time.sleep(2)
        countinue = True
        while countinue:
            clear()
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
                user_input = question_window(question +
                                             '\nIf you now longer wish to play, press enter without a number or space\n',
                                             'Question')
                if user_input == '':
                    countinue = False
                    break
                try:
                    user_input = float(user_input)
                    break
                except ValueError:
                    show_window('That is not a number, try again',
                                'Not Number')
            if countinue:
                max_score = read_file('math.txt')
                if user_input == awnser:
                    score += 1
                    show_window('Good Job, that is correct\n' +
                                'Your current score is {}'.format(score),
                                'Correctly Awnsered')
                    if score == max_score:
                        show_window('Good Job, you have hit the max score!',
                                    'Equal to High Score')
                    elif score < max_score:
                        show_window('You still have {} to go before you hit the max score'.format(max_score - score),
                                    'Less then High Score')
                    elif score > max_score:
                        show_window('You are {} over the current top score'.format(score - max_score),
                                    'Greater then high score')
                else:
                    show_window('Bad Job, that is incorrect\n' +
                                'The correct awnser is {}, and yours was {}\n'.format(awnser, user_input) +
                                'Your current score is {}'.format(score),
                                'Incorrect')
        max_score = read_file('math.txt')
        if score > max_score:
            show_window('You beat the current high score by {}'.format(score - max_score),
                        'Beat High Score')
            write_file('math.txt', score)
            logging('Player {} beat the max score (of {}) and set a new max score as {}'.format(self.username,
                                                                                                max_score,
                                                                                                score))

    def lowest_common_multiple(self):
        logging('user is operating the lowest common multiple program')
        self.login_checker()
        numb = number_input_local('The first number you want to check')
        numb2 = number_input_local('The second number you want to check')
        ma = number_input_local('Max amount of loops (Greater the number, greater the time.)')
        result = check_lowest_common_multiple(numb, numb2, ma)
        if result is False:
            show_window('The program could not find a result in the max of {} you gave.'.format(ma),
                        'Failed Result')
        else:
            show_window('The lowest common multiple between {} and {} is {}'.format(numb, numb2, result),
                        'Result')

    def add_user(self):
        self.login_checker()
        if not self.clearance_check(100):
            show_window("You don't have high enough clearnance (100)",
                        'Not enough clearance')
            logging('User {} tried and failed, with too little clearance of {} to add a new user'.format(self.username,
                                                                                                         self.security_clearence))
            return
        logging('user {} is adding a new user'.format(self.username))
        username = question_window("Enter the new user's username",
                                   'Username')
        password = question_window("Enter the new user's password",
                                   'Password')
        clearance = number_input_local("Enter the new user's clearance")
        name = question_window("What is the new user's name?",
                               'Name')
        key = number_input_local("Enter the new user's encryption key")
        name = pyWrskp.encrypt(key, name)
        username = pyWrskp.encrypt(key, username)
        password = pyWrskp.encrypt(key, password)
        clearance = pyWrskp.encrypt(key, clearance)
        username_name = pyWrskp.encrypt(key, 'user')
        password_name = pyWrskp.encrypt(key, 'password')
        clearance_name = pyWrskp.encrypt(key, 'clearance')
        name_name = pyWrskp.encrypt(key, 'name')
        current_users = read_file('txt.txt')
        current_users.append({username_name: username,
                              password_name: password,
                              clearance_name: clearance,
                              'key': key,
                              name_name: name})
        write_file('txt.txt', current_users)

    def mastermind(self):
        self.login_checker()
        logging('User is playing mastermind')
        secret_code = create_secret_code()
        show_window('| means correct, and correct place\n' +
                    '/ means correct, and wrong place\n' +
                    '- means wrong',
                    'Rules')
        max_guess = number_input_local('How many guesses do you want to be able to have?')
        guessed = False
        guesses = 0
        while True:
            player_guess_str = question_window('Input your guess use : to seperate numbers\n' +
                                               'The options are numbers 1 to 10',
                                               'Guess Input')
            player_guess_temp = player_guess_str.split(':')
            player_guess = []
            for item in player_guess_temp:
                temp = int(item)
                player_guess.append(temp)
            clear()
            guess = ('{} {} {} {} {}'.format(player_guess[0],
                                             player_guess[1],
                                             player_guess[2],
                                             player_guess[3],
                                             player_guess[4]))

            print_string = ''
            count = 0
            for item in player_guess:
                found = False
                if item == secret_code[count]:
                    print_string += '| '
                    found = True
                else:
                    for i in secret_code:
                        if item == i:
                            print_string += '/ '
                            found = True
                if not found:
                    print_string += '- '
                count += 1
            show_window(guess + '\n' + print_string,
                        'Result')
            guesses += 1
            if print_string == '| | | | | ':
                guessed = True
                break
            if guesses >= max_guess:
                break

        if guessed:
            show_window('Good Job!\n' +
                        'You won!\n' +
                        'You had {} guesses left!\n'.format(max_guess - guesses),
                        'You Won!')
            logging('User won mastermind with {} guesses out of a max of {}'.format(guesses, max_guess))
        else:
            show_window('You lost!\n' +
                        'Here is the code:\n' +
                        '{} {} {} {} {}'.format(secret_code[0],
                                                secret_code[1],
                                                secret_code[2],
                                                secret_code[3],
                                                secret_code[4]),
                        'You Lost')
            logging('User lost mastermind')


m = Main()
m.hub()
