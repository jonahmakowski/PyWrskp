import turtle

def display():
    turtle.color('orange')
    turtle.penup()
    turtle.setpos(-200, -200)
    turtle.pendown()
    turtle.goto(0, 200)
    turtle.goto(200, -200)
    turtle.goto(-200, -200)

display()
