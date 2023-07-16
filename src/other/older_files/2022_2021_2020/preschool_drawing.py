from random import randint as random
import turtle
from time import sleep

screen = turtle.Screen()
DIS_WIDTH = 1280
DIS_HEIGHT = 750
x_max = DIS_WIDTH
y_max = DIS_HEIGHT
screen.setup(DIS_WIDTH, DIS_HEIGHT)

turtles = {}
colors = ['black','blue','yellow','green','purple','orange','gold']

for i in range(len(colors)):
    t = turtle.Turtle()
    turtles['turtle' + str(i)] = t
    turtles['turtle' + str(i)].color(colors[i])
    turtles['turtle' + str(i)].speed(0)
d = 0

while True:
    for i in range(10):
        for i in range(len(turtles)):
            turtles['turtle' + str(i)].forward(random(10, 15))
            turtles['turtle' + str(i)].left(random(1, 90))
            sleep(1 / len(turtles))
    for i in range(10):
        for i in range(len(turtles)):
            turtles['turtle' + str(i)].forward(random(10, 15))
            turtles['turtle' + str(i)].right(random(1, 90))
            sleep(1 / len(turtles))
