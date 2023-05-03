import turtle


class Google:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.size = 2
        self.t.penup()
        self.current_x = -200 * self.size
        self.current_y = 200 * self.size
        if self.current_y > 500:
            self.current_y = 500
        if self.current_x > 800:
            self.current_x = 800
        self.diffrence = 125 * self.size
        self.t.speed(0)  # makes turtle go faster remove later

    def drawg(self):
        self.t.setheading(180)
        self.t.pendown()
        for i in range(270):
            self.t.forward(1*self.size)
            self.t.left(1)
        self.t.left(90)
        self.t.forward(60*self.size)
        self.t.penup()

    def drawo(self):
        self.t.setheading(180)
        self.t.pendown()
        for i in range(400):
            self.t.forward(1*self.size)
            self.t.left(1)
        self.t.penup()

    def drawl(self):
        self.t.pendown()
        self.t.setheading(270)
        self.t.pendown()
        self.t.forward(115*self.size)
        self.t.left(90)
        self.t.forward(75*self.size)
        self.t.penup()

    def drawe(self):
        self.t.pendown()
        main_distance = 115*self.size
        self.t.setheading(270)
        self.t.pendown()
        self.t.forward(main_distance)
        self.t.left(90)
        self.t.forward(75*self.size)
        self.t.backward(75*self.size)
        self.t.right(90)
        self.t.backward(main_distance/2)
        self.t.left(90)
        self.t.forward(50*self.size)
        self.t.backward(50*self.size)
        self.t.right(90)
        self.t.backward(main_distance/2)
        self.t.left(90)
        self.t.forward(75*self.size)
        self.t.penup()

    def drawgoogle(self):
        self.t.goto(self.current_x, self.current_y)
        self.current_x += self.diffrence
        self.drawg()

        for i in range(2):
            self.t.goto(self.current_x, self.current_y)
            self.current_x += self.diffrence
            self.drawo()

        self.t.goto(self.current_x, self.current_y)
        self.current_x += self.diffrence / 2
        self.drawg()

        self.t.goto(self.current_x, self.current_y)
        self.current_x += self.diffrence
        self.drawl()

        self.t.goto(self.current_x, self.current_y)
        self.current_x += self.diffrence
        self.drawe()

        input()


g = Google()
g.drawgoogle()
