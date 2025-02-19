from random import randint as r
import time


def math_game(coins):
    opration = r(1, 4)
    num_1 = r(0, 9999999)
    num_2 = r(0, 9999999)
    if opration == 1:
        opration = '+'
        question = '{} {} {}'.format(num_1, opration, num_2)
        a = str(num_1 + num_2)
    elif opration == 2:
        opration = '-'
        question = '{} {} {}'.format(num_1, opration, num_2)
        a = str(num_1 - num_2)
    elif opration == 3:
        opration = '*'
        question = '{} {} {}'.format(num_1, opration, num_2)
        a = str(num_1 * num_2)
    elif opration == 4:
        opration = '/'
        question = '{} {} {}'.format(num_1, opration, num_2)
        a = str(num_1 / num_2)
    else:
        print('error')
        question = 'error'  # this is to solve an error found by pycharm
        a = 'error'  # this is to solve an error found by pycharm
        exit(404)
    g = input('What is ' + question + '?')
    if g == a:
        print('Good job you got it correct! you earned 10 coins')
        coins += 10
        print('You now have {} coins'.format(coins))
    else:
        print('You got it incorrect, you lost 5 coins')
        coins -= 5
        print('You now have {} coins'.format(coins))
        if g == '':
            print('if you are playing basic mode this coins will be returned')
    return g, coins

def basic_math_game():
    print('WELCOME TO')
    print("JONAH'S MATH GAME!")
    print('entering nothing will end the game!')
    coins = 0
    while True:
        g, coins = math_game(coins)
        if g == '':
            coins += 5
            return

    print('GAME OVER')
    print('You have {} coins right now'.format(coins))

def challange_math_game(people):
    scores = {}
    while len(people) > 0:
        current_player = people[0]
        print('Your turn {}'.format(current_player))
        time.sleep(1)
        coins = 0
        for i in range(4):
            g, coins = math_game(coins)
        scores[current_player] = coins
        del people[0]

    print('Final scores:')
    for person in scores:
        print(str(person) + ': ' + str(scores[person]))
