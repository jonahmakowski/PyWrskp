import turtle

t = turtle.Turtle()

max = 700

length = max

t.speed(0)

t.penup()
t.goto(-400, 400)
t.pendown()

while True:
    t.forward(length)
    t.right(90)
    length -= 1
    if length < max * -1:
        break

input()
