import turtle


class Grid:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.pensize(1)
        self.draw_grid()
        self.found_cors = []

    def draw_grid(self):
        self.t.penup()
        self.t.goto(-400, 0)
        self.t.pendown()

        for t in range(20):
            self.t.forward(20)
            self.t.right(90)
            self.t.penup()
            self.t.forward(10)
            self.t.write(t + 1)
            self.t.backward(10)
            self.t.left(90)
            self.t.pendown()

        for i in range(19):
            self.t.left(90)
            self.t.penup()
            self.t.forward(20)
            self.t.left(90)
            self.t.pendown()
            self.t.forward(400)
            self.t.penup()
            self.t.backward(400)
            self.t.right(180)

        xcor = self.t.xcor()
        ycor = self.t.ycor()
        self.t.right(90)

        self.t.backward(20)

        for t in range(20):
            self.t.forward(20)
            self.t.left(90)
            self.t.penup()
            self.t.forward(10)
            self.t.write(20 - t)
            self.t.backward(10)
            self.t.right(90)
            self.t.pendown()

        self.t.goto(xcor, ycor)

        for i in range(20):
            self.t.right(90)
            self.t.forward(20)
            self.t.left(90)
            self.t.forward(380)
            self.t.backward(380)

    def find_cor(self, xcor, ycor):
        if xcor > 20 or ycor > 20:
            print('number too high')
            return
        elif xcor < 1 or ycor < 1:
            print('number too low')
            return
        xcor = xcor * 20 - 400
        ycor = ycor * 20 - 20
        self.t.shape('circle')
        self.t.penup()
        self.t.goto(xcor, ycor)
        self.t.stamp()
        self.found_cors.append([xcor, ycor])

    def draw(self):
        self.t.pensize(5)

        if len(self.found_cors) > 2:
            self.t.penup()

            for item in self.found_cors:
                temp_xcor = item[0]
                temp_ycor = item[1]
                self.t.goto(temp_xcor, temp_ycor)
                self.t.pendown()

            self.t.goto(self.found_cors[0][0], self.found_cors[0][1])

        elif len(self.found_cors) == 1:
            print('There is only one dot, so this does not work')
            self.t.pensize(1)
            return
        elif len(self.found_cors) == 2:
            self.t.penup()
            self.t.goto(self.found_cors[0][0], self.found_cors[0][1])
            self.t.pendown()
            self.t.goto(self.found_cors[1][0], self.found_cors[1][1])
        self.t.pensize(1)

        for i in range(len(self.found_cors)):
            del self.found_cors[i - 1]


C = Grid()

while True:
    do = input('Would you like to draw or find location?\n')
    if do == 'find location' or do == 'find':
        xcor = int(input('What would you like the xcor to be?'))
        ycor = int(input('What would you like the ycor to be?'))
        C.find_cor(xcor, ycor)
    elif do == 'draw':
        C.draw()
