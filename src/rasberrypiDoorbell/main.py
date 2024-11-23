from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def main():
    subprocess.run(['play', '-q', 'doorbell.wav'])
    return '<h1>Rang Doorbell!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
