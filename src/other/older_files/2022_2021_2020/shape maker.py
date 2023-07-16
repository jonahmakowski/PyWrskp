import turtle

t = turtle.Turtle()

t.right(90)
t.penup()
t.forward(100)
t.left(90)
t.pendown()

t.speed(1)

sides = int(input('How many sides would you like?\n'))
length_sides = int(input('How long would you like the sides to be?\n'))

for i in range(sides):
    t.left(360 / sides)
    t.forward(length_sides)
