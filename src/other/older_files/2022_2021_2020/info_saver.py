import json


class InfoSaver:
    def __init__(self):
        self.loc = '../../docs/txt-files/info_saver.txt'
        self.save_info = self.load(self.loc)
        self.mainloop()

    def mainloop(self):
        user_type = input('are you a new or old user? (n/o)')
        if user_type == 'n':
            username = input('What is the username you wish to set?')
            try:
                testing = self.save_info[username]
                print('This username is being used')
                exit(404)
            except KeyError:
                print('Username granted')
            password = input('What do you wish the password to be?')
            self.save_info[username] = {'password': password, 'info': []}
            self.save(self.loc, self.save_info)
            print('Info Saved')
        else:
            username = input('What is the Username?')
            password = input('What is the Password')
        do = input('What do you wish to do?')

        try:
            testing = self.save_info[username]
            if testing['password'] == password:
                print('Good job, moving on')
            else:
                print('Password is wrong')
                exit(404)
        except KeyError:
            print('This username does not exist')
            exit(404)
        if do == 'add':
            info = input('What do you wish to add?')
            self.save_info[username]['info'].append(info)
            self.save(self.loc, self.save_info)
            print('your info {} is saved'.format(info))
        elif do == 'print':
            self.save_info = self.load(self.loc)
            for item in self.save_info[username]['info']:
                print(item)

    def load(self, loc):
        with open(loc) as json_file:
            item = json.load(json_file)
        return item

    def save(self, loc, item):
        with open(loc, 'w') as outfile:
            json.dump(item, outfile)


info = InfoSaver()
