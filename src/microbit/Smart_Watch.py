from microbit import *
import music
import time

current_hrs = 21
current_mins = 47
prev_ms = time.ticks_ms()

def change_time():
    music.play(music.BA_DING)
    display.clear()
    global current_hrs, current_mins, prev_ms
    display.scroll('Change Time')
    current_hrs = 0
    current_mins = 0
    display.scroll('Hrs:')
    while not button_b.is_pressed():
        display.scroll(current_hrs)
        if button_a.was_pressed():
            current_hrs += 1
        if current_hrs >= 24:
            current_hrs = 0
    
    display.scroll('Mins:')
    while not button_b.is_pressed():
        display.scroll(current_mins)
        if button_a.was_pressed() or button_a.is_pressed():
            current_mins += 1
        if current_mins >= 60:
            current_mins = 0
    prev_ms = time.ticks_ms()
    display.scroll('Confirmed')

def show_time():
    display.clear()
    music.play(music.BA_DING)
    display.scroll('{}:{}'.format(current_hrs, current_mins))

def show_temp():
    display.clear()
    music.play(music.BA_DING)
    display.scroll('{}'.format(temperature()))

def do_time():
    global prev_ms, current_hrs, current_mins
    if abs(time.ticks_ms() - prev_ms) > 60000:
        current_mins += 1
        prev_ms += 60000
    if current_mins > 60:
        current_hrs += 1
        current_mins = 0
    if current_hrs > 24:
        current_hrs = 0

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        change_time()
    elif button_a.is_pressed():
        show_time()
    elif button_b.is_pressed():
        show_temp()

    do_time()
        
        
