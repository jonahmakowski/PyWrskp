from random import shuffle
import turtle

print('Normal edition')
input('press enter to countinue')

people = ['Brad', 'Dylan', 'Elias', 'Jonah', 'Mahathi', 'Michael', 'Nathan', 'Yonas', 'John']
shuffle(people)
print('Randomly sorted')
print(people)

print()

people.sort(reverse=True)
print('Reverse Sorted')
print(people)

print()

people.sort()
print('Sorted')
print(people)

print('Creative edition')
input('press enter to countinue')

t = turtle.Turtle()
commands = []
distance = []

while True:
    while True:
        command = input('What command would you like to use? (forward, backward, left, or right)\n')
        if (command == 'forward' or command == 'backward') or (command == 'left' or command == 'right'):

for i in range(0, len(commands)-1):
    if commands[i] == 'forward':
        t.forward(distance[i])
    elif commands[i] == 'right':
        t.right(distance[i])
    elif commands[i] == 'backward':
        t.backward(distance[i])
    elif commands[i] == 'left':
        t.left(distance[i])
