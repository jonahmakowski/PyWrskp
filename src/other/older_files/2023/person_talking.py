import turtle

t = turtle.Turtle()

def draw_person():
    t.speed(0)

    t.penup()
    t.goto(0, -100)
    t.left(90)

    #drawing of the body
    t.speed(0)
    t.pendown()
    t.forward(150)

    #drawing of the head
    t.right(90)
    for i in range(200):
        t.forward(1)
        t.left(360/200)

    #drawing of the arms
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.backward(100)
    t.forward(50)

    #drawing of the legs
    t.left(90)
    t.forward(100)
    t.right(45)
    t.forward(50)
    t.backward(50)
    t.left(90)
    t.forward(50)
    t.backward(50)
    t.right(45)

draw_person()

#drawing a speech bubble
t.penup()
t.goto(-150, 100)
t.write("Ha Ha \nI'm the bestest!")
t.forward(10)
t.left(90)
t.pendown()
t.forward(75)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(25)
t.forward(75)
t.goto(0, 75)
t.goto(-74.9999999999993, 140.00000000000028)
