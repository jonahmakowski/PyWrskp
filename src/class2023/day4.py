from random import randint, choice

print('General Homework')

guessed = False
secret = randint(0, 100)
name = input('What is your name?\n')
while True:
    guesses = input('How many guesses would you like {}?\n'.format(name))
    if guesses.isdigit():
        guesses = int(guesses)
        break
    else:
        print('Wow {} you really are a student!'.format(name))
        print('That is obviously supposed to be a number, you should be ashamed of yourself.')

print('Welcome to guess my number {}! You have {} guesses! The number is betweeen 0, and 100'.format(name, guesses))

for i in range(1, guesses + 1):
    while True:
        guess = input('Guess #{}?\n'.format(i))
        if guess.isdigit() and 0 <= int(guess) <= 100:
            guess = int(guess)
            break
        else:
            print('Wow {} you really are a student!'.format(name))
            print('That is obviously supposed to be a number, you should be ashamed of yourself.')
    if guess == secret:
        print('Good job! You won on guess number {}'.format(i))
        guessed = True
        break
    elif guess > secret:
        print('To high')
    elif guess < secret:
        print('To low')

if not guessed:
    print('You failed')
    print('The number was {} you STUDENT!'.format(secret))


print('Rock Paper scissors')
print('With dictionary, more customaziable')
input('press enter to continue')

while True:
    rounds_amount = input('How many round would you like to play {}?\n'.format(name))
    if rounds_amount.isdigit():
        rounds_amount = int(rounds_amount)
        break
    else:
        print('Wow {} you really are a student!'.format(name))
        print('That is obviously supposed to be a number, you should be ashamed of yourself.')

options = [{'name': 'rock', 'beats': 'scissors', 'lose': 'paper'},  # change this dictionary to make your own version!
           {'name': 'paper', 'beats': 'rock', 'lose': 'scissors'},
           {'name': 'scissors', 'beats': 'paper', 'lose': 'rock'}]

for cur_round in range(1, rounds_amount + 1):
    computer = options[randint(0, len(options)-1)]
    good_input = False
    while not good_input:
        player = input('{}, choose rock, paper or scissors?\n'.format(name))
        player = player.lower()
        for item in options:
            if item['name'] == player:
                player = item
                good_input = True
        if not good_input:
            print('Wow {} you really are a student!'.format(name))
            print('Again, the options are rock, paper or scissors.')
    if player['name'] == computer['beats']:
        print('The computer wins!')
    elif player['name'] == computer['lose']:
        print('You win!')
    else:
        print('its a tie!')
    print('Computer choose {}'.format(computer['name']))

print('Simple way')
input('press enter to continue')

for i in range(1, rounds_amount + 1):
    computer = choice(['rock', 'paper', 'scissors'])
    good_input = False
    while not good_input:
        player = input('{}, choose rock, paper or scissors?\n'.format(name))
        player = player.lower()
        if (player == 'rock' or player == 'paper') or player == 'scissors':
            break
        if not good_input:
            print('Wow {} you really are a student!'.format(name))
            print('Again, the options are rock, paper or scissors.')
    if player == 'rock' and computer == 'paper':
        print('Computer Won!')
    elif player == 'paper' and computer == 'scissors':
        print('Computer Won!')
    elif player == 'scissors' and computer == 'rock':
        print('Computer Won!')
    elif computer == 'rock' and player == 'paper':
        print('You Won!')
    elif computer == 'paper' and player == 'scissors':
        print('You Won!')
    elif computer == 'scissors' and player == 'rock':
        print('You Won!')
    print('The computer choose {}'.format(computer))
