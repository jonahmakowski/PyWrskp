import random
import threading
import json
import pygame
from psg_helper import *

# By this I mean functions that are only used
# once for a purpose that could be easily in main.py


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

        print('Info, Datetime')  # TODO transfer this to PSG
        for item in logs[start_idx:end_idx]:
            print('{}, {}'.format(item['log'], item['datetime']))

        if end_idx >= len(logs):
            break

        user_input = input('\nPress "n" for next page, or "q" to quit: ')

        if user_input == 'n':
            page += 1
        elif user_input == 'q':
            break


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


def play_music(music=None):
    if music is None:
        music = input('What is the name of the file you would like to play\n' +
                      'Music file must be under the "music" folder\n')
    pygame.init()
    while True:
        try:
            pygame.mixer.music.load('music/{}'.format(music))
            pygame.mixer.music.play()
            question_window('Press enter to stop playing music',
                            'Press enter to continue')
            pygame.mixer.music.stop()
            break
        except pygame.error:
            show_window('That file does not exist',
                        'Song does not exist')
            if music is None:
                music = question_window('What is the name of the file you would like to play',
                                        'Input new song')
            else:
                return


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
