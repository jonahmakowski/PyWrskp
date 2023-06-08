import turtle

def squares():
    turtle.penup()
    turtle.goto(100, 100)
    turtle.pendown()
    for i in range(180, 0, -30):
        turtle.penup()
        turtle.setpos(-i, i)
        turtle.pendown()
        
        turtle.seth(0)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        
        turtle.penup()
        turtle.setpos(-i, -i+60)
        turtle.pendown()
        
        turtle.seth(0)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
    turtle.hideturtle()
        

squares()