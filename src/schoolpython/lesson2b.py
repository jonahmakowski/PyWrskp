import turtle

turtle.screensize(300, 300)

tbr = turtle.Turtle() # Turtle Bottom Right
tbl = turtle.Turtle() # Turtle Bottom Left
ttr = turtle.Turtle() # Turtle Top Right
ttl = turtle.Turtle() # Turtle Top Left
tc = turtle.Turtle() # Turtle Center

'''
# Set to max speed
tbr.speed(0)
tbl.speed(0)
ttr.speed(0)
ttl.speed(0)
tc.speed(0)
'''

# Set colors
tbr.color('blue')
tbl.color('green')
ttr.color('purple')
ttl.color('black')
tc.color('orange')

# Pens up
tbr.penup()
tbl.penup()
ttr.penup()
ttl.penup()
tc.penup()

# Goto Correct Positions
tbl.goto(-581, -237) # DONE
tbr.goto(576, -236) # Done
ttr.goto(576, 242) # Done
ttl.goto(-581, 242) # DONE
tc.goto(50, 50) # DONE

# Put pens down
tbr.pendown()
tbl.pendown()
ttr.pendown()
ttl.pendown()
tc.pendown()

# Some turtles need to do a 180, to make the angle right
tbr.right(0)
tbl.right(180)
ttr.right(0)
ttl.right(180)
tc.right(180)

# Define radius used for the circles
radius = 50

# Draw the circles (bottom left, top right)
tbl.forward(50)
ttr.forward(50)

tbl.circle(radius)
ttr.circle(radius)

tbl.backward(50)
ttr.backward(50)

# Draw circles (bottom right, top left)
ttl.right(90)
ttl.forward(100)
ttl.left(90)
ttl.forward(50)
ttl.circle(radius)
ttl.backward(50)
ttl.right(90)
ttl.backward(100)
ttl.left(90)

tbr.right(90)
tbr.forward(100)
tbr.left(90)
tbr.forward(50)
tbr.circle(radius)
tbr.backward(50)
tbr.right(90)
tbr.backward(100)
tbr.left(90)

# Draw Circles (Center)

tc.forward(50)

tc.circle(radius)

tc.backward(50)

# Draw the squares
tbr.forward(100)
tbl.forward(100)
ttr.forward(100)
ttl.forward(100)
tc.forward(100)

tbr.right(90)
tbl.left(90)
ttr.left(90)
ttl.right(90)
tc.left(90)

tbr.forward(100)
tbl.forward(100)
ttr.forward(100)
ttl.forward(100)
tc.forward(100)

tbr.right(90)
tbl.left(90)
ttr.left(90)
ttl.right(90)
tc.left(90)

tbr.forward(100)
tbl.forward(100)
ttr.forward(100)
ttl.forward(100)
tc.forward(100)

tbr.right(90)
tbl.left(90)
ttr.left(90)
ttl.right(90)
tc.left(90)

tbr.forward(100)
tbl.forward(100)
ttr.forward(100)
ttl.forward(100)
tc.forward(100)

tbr.right(90)
tbl.left(90)
ttr.left(90)
ttl.right(90)
tc.left(90)

# Make turtles vanish
tbr.hideturtle()
tbl.hideturtle()
ttr.hideturtle()
ttl.hideturtle()
tc.hideturtle()

