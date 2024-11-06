import turtle

def display_example():
    turtle.color('red')
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.home()

class Shapes:
    def __init__(self, shape=None):
        self.shape = shape
        if self.shape != None:
            if self.shape == 'rectange_portriat':
                self.rectange_portriat()
    def rectange_portriat(self):
        turtle.penup()
        turtle.home()
        turtle.pendown()
        turtle.seth(90)
        turtle.forward(75)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(75)
    def rectange_landscape(self):
        turtle.penup()
        turtle.home()
        turtle.pendown()
        turtle.seth(0)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(100)
    def starcase(self):
        turtle.penup()
        turtle.home()
        turtle.pendown()
        turtle.seth(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)

#display_example()
#s = Shapes()
#s.rectange_portriat()
#s.rectange_landscape()
#s.starcase()
