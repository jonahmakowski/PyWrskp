from flask import Flask
import playsound

app = Flask(__name__)

@app.route('/')
def main():
    playsound.playsound('doorbell.wav', block=False)
    return '<h1>Rang Doorbell!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')