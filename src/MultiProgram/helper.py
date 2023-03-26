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
    
    for item in list_encrypt:
        key = item['key']
        count = 0
        end.append({})
        for i in item:
            if i != 'key':
                i_key = e.decrypt(i, key)
                i_decrypt = e.decrypt(item[i], key)
                end[0][i_key] = i_decrypt
            count += 1
    return end


def read_file(path):
    try:
        with open(path) as json_file:
            info = json.load(json_file)
        return info
    except FileNotFoundError:
        return []


def write_file(path, save):
    with open(path, 'w') as outfile:
        json.dump(save, outfile)


def logging(log_item):
    past_log = read_file('log.txt')
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    current_log = past_log + [{'log': log_item, 'datetime': now}]
    write_file('log.txt', current_log)


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


def number_input(question, t='int'):
    while True:
        try:
            if t == 'int':
                a = int(input(question + '\n'))
            else:
                a = float(input(question + '\n'))
            break
        except ValueError:
            print('That is not a number!')
            print('Try again!')
    return a

