import turtle
import time

t = turtle.Turtle()

i = 1
while True:
    t.write(i)
    i += 1
    time.sleep(0.1)
    t.clear()
