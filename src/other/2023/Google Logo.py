import turtle

t = turtle.Turtle()
t.shape('turtle')
size = 3
t.shapesize(size, size, size)
t.penup()
current_x = -200
diffrence = 125
t.goto(current_x, 200)
current_x += diffrence
#t.speed(0) # makes turtle go faster remove later

def drawG():
    global t
    t.setheading(180)
    t.pendown()
    for i in range(270):
        t.forward(1)
        t.left(1)
    t.left(90)
    t.forward(60)
def drawO():
    global t
    t.setheading(180)
    t.pendown()
    for i in range(400):
        t.forward(1)
        t.left(1)

def drawL():
    global t
    t.setheading(270)
    t.pendown()
    t.forward(100)
    t.left(90)
    t.forward(50)

drawG()

t.penup()
t.goto(current_x, 200)
current_x += diffrence
drawO()

t.penup()
t.goto(current_x, 200)
current_x += diffrence
drawO()

t.penup()
t.goto(current_x, 200)
current_x += diffrence
drawG()

t.penup()
t.goto(current_x, 200)
current_x += diffrence
drawL()