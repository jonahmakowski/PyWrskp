from random import randint

print('Basic Homework:')
guessed = False
name = input('What is your name?\n')
while True:
    guesses = input('How many guesses would you like {}?'.format(name))
    if guesses.isdigit():
        guesses = int(guesses)
        break
    else:
        print('Wow {} you really are a student!'.format(name))
        print('That is obviously supposed to be a number, you should be ashamed of yourself.')

print('Welcome to guess my number {}! You have {} guesses!'.format(name, guesses))

for i in range(1, guesses + 1):
    pass
