from flask import Flask
from flask import render_template, redirect, url_for, session, request, Response
from flask_sse import sse
from helper import *

# Run "gunicorn --config gunicorn.conf.py main:app" for production server (from within this folder)

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
    data = {'message': message,
            'user_sent': other_user.lower()}
    sse.publish(data, type='personal', channel=username)

@app.route('/chat')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', username=session['username'], sidebar_options=user_pages(users))

@app.route('/chat/<user>')
def chat(user):
    return render_template('home.html', username=session['username'], sidebar_options=user_pages(users), chat=user.lower())

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

@app.route('/trigger')
def trigger():
    send_message('Test', 'Jonah', 'Jonah')
    return 'Attempted Send'

if __name__ == "__main__":
    app.run()
