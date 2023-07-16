import turtle

t = turtle.Turtle()

t.speed(0)

pensize = 1

for i in range(100):
    t.forward(100)
    t.left(70)
    t.pensize(pensize)
    pensize += 0.05

t.penup()
t.goto(50, 75)
t.write('The Strange Circle')

input()
