import turtle
from time import sleep

t = turtle.Turtle()

colors = ['yellow', 'green', 'blue', 'red']
curve = 3
t.speed(0)
color = 0
heading = 90

for i in range(len(colors)):
    t.setheading(heading)
    t.fillcolor(colors[color])
    t.begin_fill()
    t.goto(0, 0)
    t.color(colors[i])
    for c in range(50):
        t.left(curve)
        t.forward(5)
    t.goto(0, 0)
    t.end_fill()
    color += 1
    t.right(1)
    if heading == 270:
        heading = 0
    else:
        heading += 90
t.penup()
t.goto(1000, 1000)

sleep(10)
