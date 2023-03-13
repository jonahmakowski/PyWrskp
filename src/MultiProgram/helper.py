import json
import datetime


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
        count_dic = 0
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
