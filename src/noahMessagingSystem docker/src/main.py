import ollama
from flask import Flask
from flask import render_template, redirect, url_for, session, request, Response
from flask_sse import sse
from helper import *

# Run "gunicorn --config gunicorn.conf.py main:app" for production server (from within this folder)
# Run "redis-server" before starting the code

users = load_users()

'''
Chats format:
chats = [{'usernames': [username1, username2], 'chat':[{'username': 'user', 'message': 'Message'}]}]
'''

app = Flask(__name__)
app.secret_key = 'your-secret-key'
app.config["REDIS_URL"] = "redis://localhost:6379/0"
app.register_blueprint(sse, url_prefix='/stream')

def send_message(message, username, other_user):
    try:
        data = {'message': message,
                'user_sent': other_user.lower()}
        sse.publish(data, type='personal', channel=username.lower())
        return 200
    except Exception as e:
        print("Error in send_message:", e)
        return 500

@app.route('/chat')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', username=session['username'], sidebar_options=user_pages(users))

@app.route('/chat/<user>', methods=['GET', 'POST'])
def chat(user):
    if 'username' not in session:
        return redirect(url_for('login'))

    user = user.title()

    if request.method == 'POST':
        if user != 'Ai':
            message = request.form['message']
            chats = load_chats_from_file()
            chats = add_to_chat_dic(chats, session['username'], user, message)
            save_chats_to_file(chats)
            send_message(message_dic_to_text(chats, user, session['username']), user, session['username'])
        else:
            message = request.form['message']
            chats = load_chats_from_file()
            chats = add_to_chat_dic(chats, session['username'], user, message)
            save_chats_to_file(chats)
            chats_ai = convert_to_ai_message_system(chats, session['username'])
            new_message = ollama.chat(model='llama3.2', messages=chats_ai)['message']['content']
            new_message.replace('\t', '    ')
            chats = add_to_chat_dic(load_chats_from_file(), 'Ai', session['username'], new_message)
            save_chats_to_file(chats)
            send_message(message_dic_to_text(chats, user, session['username']), session['username'], user)

    return render_template('home.html', username=session['username'],
                           sidebar_options=user_pages(users),
                           chat=user,
                           messages=message_dic_to_text(load_chats_from_file(), user, session['username']))

@app.route('/')
def redirect_from_main():
    return redirect(url_for('home'))

@app.route('/stream')
def stream():
    return Response(sse.stream(), content_type='text/event-stream')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if in_users(users, username, password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', message='Invalid credentials')

    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/admin')
def admin_page():
    pass

if __name__ == "__main__":
    app.run(port=80)
