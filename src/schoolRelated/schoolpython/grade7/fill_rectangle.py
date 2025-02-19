import turtle

turtle.speed(0)

for i in range (0,100):
  turtle.penup()
  turtle.setpos(-478+i,-50)
  turtle.setheading(90)
  turtle.pendown()
  turtle.forward(100)

  turtle.penup()
  turtle.setpos(turtle.xcor()+1,50)
  turtle.setheading(270)
  turtle.pendown()
  turtle.forward(100)