import turtle

sides = 100

t = turtle.Turtle()

max = 10

length = max

t.speed(0)

t.penup()
t.goto(-400, 400)
t.pendown()

while True:
    t.forward(length)
    t.right(360/sides)
    length -= 0.01
    if length < max * -1:
        break

input()