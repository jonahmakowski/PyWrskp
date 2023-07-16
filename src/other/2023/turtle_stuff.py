import turtle
import time
import random


class Turtle:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.border = 250

    def grid(self):
        self.t.pd()
        def draw(t, length):
            t.pd()
            t.forward(length)
            t.left(90)
            t.pu()
            t.forward(25)
            t.left(90)
            t.forward(length)
            t.right(180)
        self.t.penup()
        self.t.goto(-500, 420)
        self.t.right(90)

        for i in range(35):
            draw(self.t, 800)

        self.t.right(90)

        for i in range(33):
            draw(self.t, 900)
        time.sleep(5)

    def shape(self):
        self.t.pd()
        sides = int(input('How many sides?'))
        length = int(input('How long?'))
        corner = 360 / sides

        self.t.pu()
        self.t.goto(0, 0)
        self.t.pd()

        for i in range(sides):
            self.t.forward(length)
            self.t.right(corner)
        time.sleep(5)

    def scribble(self, stamp):
        self.t.pd()
        self.t.shape('turtle')
        self.t.speed(0)
        self.t.pensize(2)

        blue = turtle.Turtle()
        green = turtle.Turtle()
        yellow = turtle.Turtle()
        pink = turtle.Turtle()
        purple = turtle.Turtle()
        black = turtle.Turtle()
        brown = turtle.Turtle()
        gray = turtle.Turtle()
        red = turtle.Turtle()

        blue.color('blue')
        green.color('green')
        yellow.color('yellow')
        pink.color('pink')
        purple.color('purple')
        black.color('black')
        brown.color('brown')
        gray.color('gray')
        red.color('red')
        
        blue.pu()
        green.pu()
        yellow.pu()
        pink.pu()
        purple.pu()
        brown.pu()
        gray.pu()
        red.pu()
        
        blue.goto(0, 0)
        green.goto(-self.border, self.border)
        yellow.goto(-self.border, -self.border)
        pink.goto(self.border, self.border)
        purple.goto(self.border, -self.border)
        brown.goto(0, 0)
        gray.goto(-self.border, self.border)
        red.goto(-self.border, -self.border)
        
        blue.pd()
        green.pd()
        yellow.pd()
        pink.pd()
        purple.pd()
        brown.pd()
        gray.pd()
        red.pd()

        turtles = [blue, green, yellow, pink, purple, yellow, black, brown, gray, red]

        colors = ['blue', 'green', 'yellow', 'black', 'purple', 'pink', 'brown', 'gray', 'red']

        while True:
            for item in turtles:
                item.pensize(random.randint(1, 5))
                self.t.pensize(random.randint(1, 10))
                item.shape('circle')
                if stamp == True:
                    item.stamp()
                item.speed(0)

                item.goto(random.randint(-self.border, self.border), random.randint(-self.border, self.border))

                x = item.xcor()
                y = item.ycor()

                self.t.color(colors[random.randint(0, len(colors) - 1)])
                self.t.goto(x, y)


tit = Turtle()
while True:
    do = input('What do you wish to do?\n')
    if do == 'grid':
        tit.grid()
    elif do == 'shape':
        tit.shape()
    elif do == 'scribble':
        stamp = input('Would you like to stamp? (y/n)\n')
        if stamp == 'y':
            tit.scribble(True)
        else:
            tit.scribble(False)
    else:
        print('That is not an option try again')
