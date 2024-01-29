import threading, time
from datetime import datetime

class Main:
    def __init__(self):
        self.time = 0
        time = threading.Thread(target=self.time_track())
        time.start()
        while True:
            print(self.time)
    def time_track(self):
        while True:
            self.time = datetime.now()
            time.sleep(0.25)
    
m = Main()