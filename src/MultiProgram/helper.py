import json
import datetime
import threading

import pygame
import turtle
import random


class Encrption:
    def __init__(self):
        self.abcs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                     'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                     'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                     'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '.', ',',
                     '"', "'", '1', '2', '3', '4', '5', '6', '7', '8', '9',
                     '0', '-', '_', '+', '=', '{', '}', '[', ']', '(', ')',
                     '!', '?', '|', '<', '>', '/']

    def encrypt(self, item, key):
        item_list = list(item)
        completed_list = []
        for i in item_list:
            added = False
            for t in range(len(self.abcs)):
                if i == self.abcs[t]:
                    t_key = t + key
                    if t_key <= len(self.abcs) -1:
                        completed_list.append(self.abcs[t_key])
                    else:
                        t_key_len = len(self.abcs) - t_key
                        t_key_len = t_key_len * -1
                        completed_list.append(self.abcs[t_key_len])
                    added = True
            if not added:
                completed_list.append(i)
        completed_string = ''
        for item in completed_list:
            completed_string += item
        return completed_string

    def decrypt(self, item, key):
        item_list = list(item)
        completed_list = []
        key = key * -1
        for i in item_list:
            added = False
            for t in range(len(self.abcs)):
                if i == self.abcs[t]:
                    t_key = t + key
                    if t_key <= len(self.abcs) -1:
                        completed_list.append(self.abcs[t_key])
                    else:
                        t_key_len = len(self.abcs) - t_key
                        t_key_len = t_key_len * -1
                        completed_list.append(self.abcs[t_key_len])
                    added = True
            if not added:
                completed_list.append(i)
        completed_string = ''
        for item in completed_list:
            completed_string += item
        return completed_string


def decrypt_txt(path='txt.txt'):
    e = Encrption()
    end = []
    list_encrypt = read_file(path)
    
    count = 0

    for item in list_encrypt:
        key = item['key']
        end.append({})
        for i in item:
            if i != 'key':
                i_key = e.decrypt(i, key)
                i_decrypt = e.decrypt(item[i], key)
                end[count][i_key] = i_decrypt
        count += 1
    return end


def read_file(path):
    try:
        with open(path) as json_file:
            info = json.load(json_file)
        return info
    except FileNotFoundError:
        return []


def write_log(data, path='log.txt'):
    with open(path, 'w') as f:
        for item in data:
            f.write(json.dumps(item) + '\n')


def read_log(path='log.txt'):
    with open(path) as f:
        lines = f.readlines()

    logs = []
    for line in lines:
        logs.append(json.loads(line))
    return logs


def write_file(path, save):
    with open(path, 'w') as outfile:
        json.dump(save, outfile)


def logging(log_item):
    past_log = read_log()
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    current_log = past_log + [{'log': log_item, 'datetime': now}]
    write_log(current_log)


def play_music(music=None):
    if music is None:
        music = input('What is the name of the file you would like to play\n' +
                      'Music file must be under the "music" folder\n')
    pygame.init()
    while True:
        try:
            pygame.mixer.music.load('music/{}'.format(music))
            pygame.mixer.music.play()
            input('Press enter to stop playing music')
            pygame.mixer.music.stop()
            break
        except pygame.error:
            print('That file does not exist')
            music = input('What is the name of the file you would like to play')


def check_lowest_common_multiple(num, multiple, m):

    class CustomThread(threading.Thread):
        def __init__(self, ma, numb):
            self.ma = ma
            self.numb = numb
            threading.Thread.__init__(self, target=self.loop, args=())
            self.multiples = None

        def loop(self):
            counter = 1
            current_num = 0
            multiples = []
            while counter <= self.ma:
                current_num += self.numb
                multiples.append(current_num)
                counter += 1
            self.multiples = multiples

    thread = CustomThread(m, num)
    thread2 = CustomThread(m, multiple)
    thread.start()
    thread2.start()
    thread.join()
    thread2.join()
    multiples = thread.multiples
    multiples2 = thread2.multiples

    for item in multiples:
        for item2 in multiples2:
            if item2 == item:
                return item2
    return False


def number_input(question, t='int', new_line=True):
    while True:
        try:
            if new_line:
                if t == 'int':
                    a = int(input(question + '\n'))
                else:
                    a = float(input(question + '\n'))
                break
            else:
                if t == 'int':
                    a = int(input(question))
                else:
                    a = float(input(question))
                break
        except ValueError:
            print('That is not a number!')
            print('Try again!')
    return a


def create_secret_code(amount=5):
    secret_code = []
    for i in range(amount):
        choice = random.randint(1, amount*2)
        secret_code.append(choice)
    return secret_code


def display_logs(logs):
    page_size = 10  # number of logs to display per page
    page = 0

    while True:
        start_idx = page * page_size
        end_idx = (page + 1) * page_size

        print('Info, Datetime')
        for item in logs[start_idx:end_idx]:
            print('{}, {}'.format(item['log'], item['datetime']))

        if end_idx >= len(logs):
            break

        user_input = input('\nPress "n" for next page, or "q" to quit: ')

        if user_input == 'n':
            page += 1
        elif user_input == 'q':
            break
