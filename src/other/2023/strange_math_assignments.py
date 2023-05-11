from pyWrskp import *
from random import randint
from time import sleep
import math


class StrangeMathAssignemnts:
    def __init__(self, user):
        self.user = user
    def calculator(self):
        equation = input('Input your equation:\n')
        try:
            if '+' in equation:
                equation_lis = equation.split('+')
                equation_lis[0] = float(equation_lis[0])
                equation_lis[1] = float(equation_lis[1])
                awnser = equation_lis[0] + equation_lis[1]
            elif '-' in equation:
                equation_lis = equation.split('-')
                equation_lis[0] = float(equation_lis[0])
                equation_lis[1] = float(equation_lis[1])
                awnser = equation_lis[0] - equation_lis[1]
            elif '*' in equation:
                equation_lis = equation.split('*')
                equation_lis[0] = float(equation_lis[0])
                equation_lis[1] = float(equation_lis[1])
                awnser = equation_lis[0] * equation_lis[1]
            elif '/' in equation:
                equation_lis = equation.split('/')
                equation_lis[0] = float(equation_lis[0])
                equation_lis[1] = float(equation_lis[1])
                awnser = equation_lis[0] / equation_lis[1]
            elif '^' in equation:
                equation_lis = equation.split('^')
                equation_lis[0] = float(equation_lis[0])
                equation_lis[1] = float(equation_lis[1])
                awnser = equation_lis[0] ** equation_lis[1]
            elif '$' in equation:
                equation_lis = equation.split('$')
                equation_lis[0] = float(equation_lis[0])
                awnser = math.sqrt(equation_lis[0])
            print('The anwser is:')
            print(awnser)
        except:
            print('{} is not a valid equation.'.format(equation))
            return


s = StrangeMathAssignemnts('Jonah')
s.calculator()
