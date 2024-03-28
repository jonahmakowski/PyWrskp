from flask import request, render_template, redirect
from app import app
import threading


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title='Home')

@app.route('/passwordcrack', methods=['GET', 'POST'])
def passwordcrack():
    return render_template('passwordCrack.html', title='Password Crack')