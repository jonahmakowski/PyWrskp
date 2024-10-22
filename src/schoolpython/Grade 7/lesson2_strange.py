import turtle as t

def triangles():
    count=30
    t.speed(0)
    for i in range(360*2):
        t.home()
        t.left(count)
        t.forward(400)
        t.right(120)
        t.forward(400)
        t.right(120)
        t.forward(400)
        count+=0.5
    t.hideturtle()
    
triangles()
