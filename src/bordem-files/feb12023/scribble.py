import turtle
from random import randint as r

bounds = 500
max_length = 100
turtles_amount = 10

t = turtle.Turtle()
t.speed(0)
t.color('red')
t.penup()
t.goto(bounds, bounds)
t.pendown()
t.goto(-bounds, bounds)
t.goto(-bounds, -bounds)
t.goto(bounds, -bounds)
t.goto(bounds, bounds)
t.penup()
t.goto(bounds + bounds, bounds + bounds)

turtles = []

for i in range(turtles_amount):
    turtles.append(turtle.Turtle())

for item in turtles:
    item.shape('turtle')
    item.speed(0)

while True:
    for item in turtles:
        x = item.xcor()
        y = item.ycor()
        if (int(x) > bounds or int(x) < -bounds) or (int(y) > bounds or int(y) < -bounds):
            item.penup()
            item.goto(0, 0)
            item.pendown()

        if r(1, 2) == 1:
            item.left(r(1, 180))
        else:
            item.right(r(1, 180))

        if r(1, 2) == 1:
            item.forward(r(1, max_length))
        else:
            item.forward(r(1, max_length))

        x = item.xcor()
        y = item.ycor()
        if (int(x) > bounds or int(x) < -bounds) or (int(y) > bounds or int(y) < -bounds):
            item.penup()
            item.goto(0, 0)
            item.pendown()
