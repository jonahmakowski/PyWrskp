import turtle

t = turtle.Turtle()
t.speed(0)

size = int(input('How big would you like it to be?'))

t.left(90)

t.penup()
t.backward(100)
t.pendown()

t.forward(100 * size)
t.backward(100 * size)
t.right(150)
t.forward(50 * size)
t.backward(50 * size)
t.left(300)
t.forward(50 * size)
t.backward(50 * size)
t.right(150)
t.forward(50 * size)
t.right(90)
t.forward(25 * size)
t.backward(50 * size)
t.forward(25 * size)
t.left(90)
t.forward(50 * size)
t.right(90)

for i in range(150 * size):
    t.left(360/(150 * size))
    t.forward(1 * size)

t.left(90)
t.penup()
t.forward(10 * size)
t.pendown()
t.right(90)
t.forward(10 * size)
t.backward(20 * size)
t.forward(10 * size)

t.left(90)

t.penup()

t.forward(20 * size)
t.right(90)
t.forward(10 * size)
t.pendown()
for i in range(25 * size):
    t.left(360/(25 * size))
    t.forward(0.5 * size)

t.penup()
t.backward(10 * size)
t.right(180)
t.forward(10 * size)
t.pendown()
for i in range(25 * size):
    t.right(360/(25 * size))
    t.forward(0.5 * size)

t.penup()
t.backward(100 * size)
