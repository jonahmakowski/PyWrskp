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
        unformated_usernames = f.readlines()

    usernames = []

    for string in unformated_usernames:
        usernames.append(string.strip())

    users = []

    for username in usernames:
        password = os.getenv(username)
        if password is not None:
            users.append({'user': username, 'password': os.getenv(username)})
        else:
            print('User {} does not have a defined password. Terminating'.format(username))
            exit()

    users.append({'user':'Ai', 'password':None})

    return users

def user_pages(users):
    sidebar_dic = {}
    for user in users:
        sidebar_dic[user['user']] = '/chat/{}'.format(user['user'].lower())

    return sidebar_dic

def load_chats_from_file():
    with open('chats.txt', 'r') as f:
        chats = json.load(f)

    return chats

def save_chats_to_file(chats):
    with open('chats.txt', 'w') as f:
        json.dump(chats, f)

def message_dic_to_text(ls, user1, user2):
    result = ''
    ls_new = None
    # print(user1, user2, ls)
    for chat in ls:
        if user1 in chat['usernames'] and user2 in chat['usernames']:
            chat_copy = chat['usernames'].copy()
            chat_copy.remove(user1)
            if (chat_copy == [user1] and user1 == user2) or user1 != user2:
                ls_new = chat.copy()

    if ls_new is None:
        ls_new = {"usernames": [user1, user2], "chat": []}

    for message in ls_new['chat']:
        result += '\n<u>**{}**</u>: {}'.format(message['username'], message['message'])

    return result

def add_to_chat_dic(ls, sender, respondent, message):
    found = False

    for chat in ls:
        if sender in chat['usernames'] and respondent in chat['usernames']:
            chat_copy = chat['usernames'].copy()
            chat_copy.remove(sender)
            if (chat_copy == [sender] and sender == respondent) or sender != respondent:
                chat['chat'].append({'username': sender, 'message': message})
                found = True

    if not found:
        ls.append({'usernames': [sender, respondent], 'chat':[{'username': sender, 'message': message}]})

    return ls

def clear_message_history():
    chats = load_chats_from_file()
    for chat in chats:
        chat['chat'] = []
    save_chats_to_file(chats)

def convert_to_ai_message_system(ls, user):
    chat = []
    for c in ls:
        if 'Ai' in c['usernames'] and user in c['usernames']:
            chat = c['chat']

    new_chat = [{'role':'system', 'content': 'You are an AI assistant running on a local chat platform. The other person is called {}. You can use markdown bolding and italics. You are the LLM llama3.2.'.format(user)}]
    for message in chat:
        if message['username'] == 'Ai':
            new_chat.append({'role':'assistant', 'content': message['message']})
        else:
            new_chat.append({'role':'user', 'content': message['message']})

    return new_chat

if __name__ == '__main__':
    clear_message_history()
    print('Cleared History')
