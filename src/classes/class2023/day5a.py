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
commands = []
distances = []

while True:
    while True:
        command = input('What command would you like to use? (forward, backward, left, or right)\n')
        command = command.lower()
        if (command == 'forward' or command == 'backward') or (command == 'left' or command == 'right'):
            commands.append(command)
            break
    while True:
        distance = input('What number would you like to use, for example 90 degrees right, or 100 units forward!\n')
        if distance.isdigit():
            distances.append(int(distance))
            break
    continue_loop = input('Press enter to continue, type n to stop')
    if continue_loop == 'n':
        break
    print('\n\n\n')

t = turtle.Turtle()

for i in range(0, len(commands)):
    # print('Command {}'.format(commands[i]))
    # print('Distance {}'.format(distances[i]))
    if commands[i] == 'forward':
        t.forward(distances[i])
    elif commands[i] == 'right':
        t.right(distances[i])
    elif commands[i] == 'backward':
        t.backward(distances[i])
    elif commands[i] == 'left':
        t.left(distances[i])

input('Press enter to end program')
