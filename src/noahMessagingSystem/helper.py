from dotenv import load_dotenv
import os

def in_users(users, user, password):
    for u in users:
        if u['user'] == user and u['password'] == password:
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

print(load_users())
