import json
from datetime import datetime


class Main:
    def __init__(self):
        self.user, self.password, self.clearance = self.security()
        if self.user is None:
            exit()

    def security(self):
        user = input('State Your User\n')
        password = input('State Your Password\n')
        clearance = input('State Your Clearance Level\n')
        info = self.load_file('bordem_user_info.txt')
        passed = False
        for item in info:
            if (item['user'] == user and item['password'] == password) and item['clearance'] == clearance:
                passed = True
                break
        if not passed:
            info = self.load_file('failed_logging.txt')
            now = datetime.now()
            info.append({'datetime': str(now.strftime("%d/%m/%Y %H:%M:%S")),
                         'user': user,
                         'password': password,
                         'clearance': clearance})
            self.save_file('failed_logging.txt', info)
            return None, None, None
        if passed:
            print('Clearance Granted')
            print('You have successfully been granted clearance level {}'.format(clearance))
            return user, password, clearance

    @staticmethod
    def save_file(loc, item):
        with open(loc, 'w') as outfile:
            json.dump(item, outfile)

    @staticmethod
    def load_file(loc):
        with open(loc, 'r') as json_file:
            item = json.load(json_file)
        return item


m = Main()
