import pyWrskp
from random import randint


class Games:
    def __init__(self, user):
        self.user = user
    
    def math(self):
        print('Welcome {}'.format(self.user))
        print('The current high score is {} by user {}!'.format(pyWrskp.read_file('math.txt')['score'],
                                                                pyWrskp.read_file('math.txt')['user']))
        print('If you respond anything greater or equal than 1000001, you will get your results')
        score = 0
        while True:
            num1 = randint(-100, 1000)
            num2 = randint(-100, 1000)
            operation = randint(1, 4)
            if operation == 1:
                question = '{} + {}'.format(num1, num2)
                awnser = num1 + num2
            elif operation == 2:
                question = '{} - {}'.format(num1, num2)
                awnser = num1 - num2
            elif operation == 3:
                question = '{} * {}'.format(num1, num2)
                awnser = num1 * num2
            else:
                question = '{} / {}'.format(num1, num2)
                awnser = num1 / num2
            user_input = pyWrskp.number_input(question,
                                              t='float',
                                              tell=False)
            if user_input >= 1000001:
                break
            if int(user_input) == int(awnser):
                print('That is correct!')
                score += 1
            else:
                print('That is incorrect')
            print('The awnser was {}'.format(awnser))
            print('Your score is {}'.format(score))
        print('Game ended!')
        print('You had a final score of {}!'.format(score))
        if score >= pyWrskp.read_file('math.txt')['score']:
            print('You have a greater or equal score to the current high score')
            print('You have claimed that positstion')
            pyWrskp.write_file('math.txt',
                               {'score': score, 'user': self.user})


g = Games('Noah')
g.math()
