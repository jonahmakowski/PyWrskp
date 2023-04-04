import datetime
from psg_helper import *
from main_expanded import *
from encription import *


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


def write_file(path, save):
    with open(path, 'w') as outfile:
        json.dump(save, outfile)


def logging(log_item):
    past_log = read_log()
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    current_log = past_log + [{'log': log_item, 'datetime': now}]
    write_log(current_log)


def number_input(question,
                 t='int',
                 new_line=False,
                 tell=True):
    if tell:
        question += ' (This must be a number)'
    if new_line:
        question += '\n'
    while True:
        try:
            if t == 'int':
                a = int(question_window(question,
                                        'Input Number'))
            else:
                a = float(question_window(question,
                                          'Input Number'))
            break
        except ValueError:
            show_window('That is not a number!\n' +
                        'Try again',
                        'Not a number')
    return a
