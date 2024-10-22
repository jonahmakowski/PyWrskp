import turtle

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'violet']
turtle.home()

for i in range(7):
  turtle.color(colors[i])
  turtle.pensize(15)
  turtle.seth(90)
  turtle.circle(100-i*10, 180)
  turtle.penup()
  turtle.left(90)
  turtle.fd(190-i*20)
  turtle.pendown()

turtle.hideturtle()