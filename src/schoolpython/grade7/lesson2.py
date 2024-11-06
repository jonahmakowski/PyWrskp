'''
Jonah
Mrs. Brownhill
May 26, 2023
This program is supposed to make four triangles coming out of the 0,0 point
'''

import turtle as t
'''
def triangles():
    count=30
    t.speed(0)
    for i in range(4):
        t.home()
        t.left(count)
        t.forward(100)
        t.right(120)
        t.forward(100)
        t.right(120)
        t.forward(100)
        count+=90
    t.hideturtle()
'''

def triangles():
    t.speed(0)
    
    t.home()
    t.left(30)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    
    t.home()
    t.left(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    
    t.home()
    t.left(210)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    
    t.home()
    t.left(300)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    
    t.hideturtle()
    
triangles()
