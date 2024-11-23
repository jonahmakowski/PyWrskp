from flask import Flask
import vlc

app = Flask(__name__)

@app.route('/')
def main():
    player = vlc.MediaPlayer("doorbell.wav")
    player.play()
    return '<h1>Rang Doorbell!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')