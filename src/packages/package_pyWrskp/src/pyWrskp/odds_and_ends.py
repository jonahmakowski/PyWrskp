from time import sleep
import pygame


def number_input(question,
                 t='int',
                 new_line=True,
                 tell=True,
                 message='That is not a number!\n Try again'):
    if tell:
        question += ' (This must be a number)'
    if new_line:
        question += '\n'
    while True:
        try:
            if t == 'int':
                a = int(input(question))
            else:
                a = float(input(question))
            break
        except ValueError:
            print(message)
    return a


def loading(time):
    loops = int(time * 1.5)
    for i in range(loops):
        print('|', end="\r")
        sleep(0.5)
        print('/', end="\r")
        sleep(0.5)
        print('-', end="\r")
        sleep(0.5)


def play_music(music, print_info):
    pygame.init()
    try:
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        if print_info:
            input('Press enter to stop playing music')
            pygame.mixer.music.stop()
        return True
    except pygame.error:
        if print_info:
            print('That file does not exist')
        return False
