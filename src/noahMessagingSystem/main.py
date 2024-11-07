from flask import Flask
from flask import render_template, redirect, url_for, session, request, send_from_directory
from helper import *

# Run "gunicorn --config gunicorn.conf.py main:app" for production server

users = load_users()

app = Flask(__name__)
app.secret_key = 'your-secret-key'

@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', username=session['username'])


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

if __name__ == "__main__":
    app.run()
