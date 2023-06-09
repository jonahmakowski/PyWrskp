'''
Jonah
Mrs. Brownhill
June 13, 2023
This program is supposed to make four filled in circles.
'''

import turtle as t

def squares_circles():
    t.color('purple')
    
    t.speed(0)
    t.pensize(3)
    t.penup()
    
    for y in range(10, 36):
        t.penup()
        t.goto(25, y)
        t.pendown()
        t.circle(25-y)
        
        t.penup()
        t.goto(-25, y)
        t.pendown()
        t.circle(25-y)
        
        t.penup()
        t.goto(-25, -y)
        t.pendown()
        t.circle((25-y)*-1)
        
        t.penup()
        t.goto(25, -y)
        t.pendown()
        t.circle((25-y)*-1)
        
    
    t.hideturtle()

squares_circles()
    