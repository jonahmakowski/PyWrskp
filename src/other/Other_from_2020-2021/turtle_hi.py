import turtle

t = turtle.Turtle()

t.penup
t.goto(140, 10)
t.pendown()

def hi():
    t.left(90)
    t.forward(100)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.backward(100)
    t.right(90)
    t.penup()
    t.forward(50)
    t.left(90)
    t.pendown()
    t.forward(75)
    t.penup()
    t.forward(10)
    t.pendown()
    t.forward(1)
    t.penup()
    t.right(90)
    t.forward(100)
    t.pendown()
hi()
hi()
hi()