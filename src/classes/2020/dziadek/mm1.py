# don't use file-name: turtle.py
import turtle
from random import randint
import time

t = turtle.Turtle()
t.penup()
t.goto (-140,140)
t.speed(0)
t.pendown()
screen = turtle.Screen()		# screen.setup(500,500)

# draw race-lines
for i in range (8):
	t.forward(318)
	t.backward(318)
	t.right(90)
	t.penup()
	t.forward(40)
	t.left(90)
	t.pendown()

# draw the tick finish-line
t.penup()
t.left(90)
t.forward(40)
t.right(90)
t.forward(315)
t.left(90)
t.pendown()
t.forward(280)
for l in range(10):
	t.right(90)
	t.forward(1)
	t.right(90)
	t.forward(280)
	t.backward(280)
	t.left(180)
t.penup()
t.goto(-150,200)
t.color('white')

# colors of racers, implicitly define the number of racers
colors = ['Red', 'Blue', 'Lime', 'Violet', 'Orange', 'Gray', 'Black']
n_racers = len(colors)
racers = []
x_start = -160
y_start = 120
y_current = 120
y_delta = 40
# create racers and position each of them at its start position (the corresponding line-beginning)
for col in colors:
	racer = turtle.Turtle()
	racer.shape('turtle')
	racer.color(col)
	racer.speed(0)
	racer.penup()
	racer.goto(x_start, y_current)
	racers.append(racer)
	y_current -= y_delta

# show start-preparation signal-markers and 'Go'
maker = turtle.Turtle()
maker.penup()
# maker.goto(-160,160)
maker.goto(x_start, y_start + y_delta)
maker.speed(0)
for i in range(4):
	maker.write(i)
	maker.forward(20)
	time.sleep(0.5)
maker.write('Go')
maker.color('white')
time.sleep(0.5)

# race: n_steps, at each step a random speed for each racer
n_steps = 110
for turn in range(n_steps):
	for racer in racers:
		racer.speed(randint(1,10))
		racer.forward(randint(1,5))

results = {}  # dictionary of results
for i in range(n_racers):		# store the results in the dictionary
	results[colors[i]] = int(racers[i].xcor())
# print(results)  # uncomment to see the dictionary items

# sort the results and print
from collections import Counter		 # use the Counter from the collections to sort the race results
c = Counter(results)
results_sort = c.most_common()		 # most_common() sorts the dictionary items in ascending order
# print(results_sort) # uncomment to see the unformatted sorted results
place = 1
print('Results of the race sorted by the distance:')
for item in results_sort:
	print('Place ' + str(place) + ': ' + item[0] + ',  distance = '+ str(item[1]))
	place += 1
print('Hit the return/enter key to finish.')
input()
