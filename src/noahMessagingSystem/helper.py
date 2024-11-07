from dotenv import load_dotenv
import os
import json

def in_users(users, user, password=None):
    for u in users:
        if password is not None and (u['user'] == user and u['password'] == password):
            return True
        elif password is None and u['user'] == user:
            return True
    return False

def load_users():
    load_dotenv()
    with open('usernames.txt', 'r') as f:
        usernames = f.readlines()

    users = []

    for username in usernames:
        password = os.getenv(username)
        if password is not None:
            users.append({'user': username, 'password': os.getenv(username)})
        else:
            print('User {} does not have a defined password. Terminating'.format(username))
            exit()

    return users

def user_pages(users):
    sidebar_dic = {}
    for user in users:
        sidebar_dic[user['user']] = '/chat/{}'.format(user['user'].lower())

    return sidebar_dic

def load_chats_from_file():
    with open('chats.txt', 'r') as f:
        return json.load(f)

def save_chats_to_file(chats):
    with open('chats.txt', 'w') as f:
        f.write(chats)
