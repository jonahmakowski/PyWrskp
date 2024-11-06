import sys
import json
import random
import os
sys.path.append('../coder-decoder')
from coder import CoderDecoder as Coder


'''
Need to pass a message to your friends?
Don't want anyone else to see it?
Use this program!

This program when you run the "create" option, will create a message.txt file, if your friend has the program, they can
decode the message!
'''


class Sender:
    def __init__(self):
        self.remote_coder = Coder(print_info=False)
        self.remote_coder_2 = Coder(print_info=False)
        self.remote_coder_3 = Coder(print_info=False)
        self.remote_coder_4 = Coder(print_info=False)
        self.remote_coder_5 = Coder(print_info=False)

    def create_note(self):
        print('What would you like the password to be?')
        password = input('The person who decodes this needs to know it')
        message = input('What is the message that you would like to send?')
        key = random.randint(0, len(self.remote_coder.abcs) - 1)
        key_for_the_key = random.randint(0, len(self.remote_coder.abcs) - 1)
        destroy = input('Would you like the file to be destoryed after reading?\n'
                        'Will be destroyed either way if password is inputed wrong\n'
                        'y/n\n')

        self.remote_coder.add_vars(message, key)
        message = self.remote_coder.code()

        self.remote_coder_2.add_vars(password, key)
        password = self.remote_coder_2.code()

        self.remote_coder_5.add_vars(destroy, key)
        destroy = self.remote_coder_5.code()

        self.remote_coder_3.add_vars(str(key), key_for_the_key)
        key = self.remote_coder_3.code()

        self.remote_coder_4.add_vars(str(key_for_the_key), 15)
        key_for_the_key = self.remote_coder_4.code()

        items = []
        for i in range(5):
            item = ''
            for c in range(random.randint(6, 20)):
                new_item = ''
                while (new_item != '}' and new_item != '{') and (new_item != '[' and new_item != ']'):
                    new_item = self.remote_coder.abcs[random.randint(0, len(self.remote_coder.abcs) - 1)]
                    item += new_item
            items.append(item)

        save_dic = {'dshaidsh': items[0],
                    'asuydhausdhuashd': password,
                    'shadiufad': items[1],
                    'sdifhuegtsydftyas': message,
                    'g': items[2],
                    'asdyatsdftras': key,
                    'asd7r8ushdfuhja': items[3],
                    'd': destroy,
                    'fjgishuagsdiufji': items[4],
                    'gjfosjodjif': key_for_the_key}

        with open('message.txt', 'w') as outfile:
            json.dump(save_dic, outfile)

    def read_note(self):
        try:
            with open('message.txt') as json_file:
                dic = json.load(json_file)
        except FileNotFoundError:
            print('There is no file like this (make sure it is called message.txt)')
            exit(404)

        self.remote_coder_4.add_vars(dic['gjfosjodjif'], 15)
        key_for_the_key = int(self.remote_coder_4.decode())

        self.remote_coder_3.add_vars(dic['asdyatsdftras'], key_for_the_key)
        key = int(self.remote_coder_3.decode())

        password = input('What is the password?')

        self.remote_coder_2.add_vars(dic['asuydhausdhuashd'], key)
        password_check = self.remote_coder_2.decode()

        if password != password_check:
            print('password incorrect deleting file')
            os.remove("message.txt")
            exit(500)

        self.remote_coder.add_vars(dic['sdifhuegtsydftyas'], key)
        message = self.remote_coder.decode()

        self.remote_coder_5.add_vars(dic['d'], key)
        destroy = self.remote_coder_5.decode()

        print('The message in this file is:')
        print(message)

        if destroy == 'y':
            print('destroying file')
            os.remove('message.txt')
        else:
            print('The person who sent you this .txt file has decieded that it is not nessary to delete the file,')
            print('Though you may do so if you want')


if __name__ == '__main__':
    sender = Sender()
    do = input('What do you wish to do?')
    if do == 'create':
        sender.create_note()
    elif do == 'read':
        sender.read_note()
