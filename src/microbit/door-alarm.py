from microbit import *

active_mag = False

while True:
    if compass.get_field_strength() < 200000:
        active_mag = True
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll('Confirmed')
        active_mag = False
        active_light = False
    elif button_a.is_pressed():
        if active_mag:
            display.set_pixel(0, 0, 9)
            display.set_pixel(4, 4, 9)
            display.set_pixel(0, 4, 9)
            display.set_pixel(4, 0, 9)
        else:
            display.set_pixel(2, 2, 9)
        while not button_b.is_pressed():
            pass
        display.clear()
    sleep(10)
