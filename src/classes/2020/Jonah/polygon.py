import turtle

class Polygon:
    def __init__(self, sides, side_length):
        self.sides = sides
        self.side_length = side_length
    
    def draw(self, t, loc=(0,0), fill=False):
        t.pu()
        t.goto(loc)
        t.pd()
        if fill:
            t.begin_fill()
        for s in range(self.sides):
            t.fd(self.side_length)
            t.left(360/self.sides)
        t.end_fill()
class Square(Polygon):
    def __init__(self, side_length):
        super().__init__(4, side_length)
    def show_area(self, t):
        t.write(self.side_length**2)

t = turtle.Turtle()
shape = Polygon(10, 1)
shape.draw(t)
shape.draw(t, loc=(100, 100), fill=True)
square = Square(20)
square.draw(t, loc=(200, 200))
square.show_area(t)