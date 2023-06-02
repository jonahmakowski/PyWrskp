import turtle

t = turtle.Turtle()
sides = int(input('How many sides would you like?'))
length = 0.025
turn = 360 / sides
t.speed(0)
for i in range(sides):
    t.forward(length)
    t.right(turn)

t.penup()
t.goto(10000, 100000)

input()
