import turtle

turtle.screensize(300, 300)

tbr = turtle.Turtle() # Turtle Bottom Right
tbl = turtle.Turtle() # Turtle Bottom Left
ttr = turtle.Turtle() # Turtle Top Right
ttl = turtle.Turtle() # Turtle Top Left

# Set colors
tbr.color('blue')
tbl.color('green')
ttr.color('purple')
ttl.color('black')

# Pens up
tbr.penup()
tbl.penup()
ttr.penup()
ttl.penup()
'''
tbl.goto(-200, -200)
tbr.goto(200, -200)
ttr.goto(200, 200)
ttl.goto(-200, 200)
'''

# Goto cornors
tbl.goto(-581, -237) # DONE
tbr.goto(576, -236) # Working On
ttr.goto(576, 242) # Done
ttl.goto(-581, 242) # DONE

# Put pens down
tbr.pendown()
tbl.pendown()
ttr.pendown()
ttl.pendown()

# Some turtles need to do a 180, to make the angle right
tbr.right(0)
tbl.right(180)
ttr.right(0)
ttl.right(180)

# Draw the squares
tbr.forward(100)
tbl.forward(100)
ttr.forward(100)
ttl.forward(100)

tbr.right(90)
tbl.left(90)
ttr.left(90)
ttl.right(90)

tbr.forward(100)
tbl.forward(100)
ttr.forward(100)
ttl.forward(100)

tbr.right(90)
tbl.left(90)
ttr.left(90)
ttl.right(90)

tbr.forward(100)
tbl.forward(100)
ttr.forward(100)
ttl.forward(100)

tbr.right(90)
tbl.left(90)
ttr.left(90)
ttl.right(90)

tbr.forward(100)
tbl.forward(100)
ttr.forward(100)
ttl.forward(100)

tbr.right(90)
tbl.left(90)
ttr.left(90)
ttl.right(90)

# Make turtles vanish
tbr.hideturtle()
tbl.hideturtle()
ttr.hideturtle()
ttl.hideturtle()
