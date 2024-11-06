import game_extras
from random import randint as r

class Game:
    def __init__(self):
        while True:
            try:
                self.max = int(input('What would you like the max of the nums\n'))
                break
            except:
                print('ERROR: this is not a number, try again')
        while True:
            try:
                self.min = int(input('What would you like the min of the nums\n'))
                break
            except:
                print('ERROR: this is not a number, try again')
        self.neg = input('Would you like negitive numbers and decimal numbers? (y/n)\n')
        self.money = 0
        self.wrong = 0
        self.correct = 0
        
        while self.wrong <= 20:
            option = r(1, 4)
            if option == 1:
                self.add()
            elif option == 2:
                self.sub()
            elif option == 3:
                self.multi()
            elif option == 4:
                self.div
        self.over()
    
    def add(self):
        num1, num2, a = game_extras.add(self.max, self.min)
        
        while True:
            try:
                ask = int(input('What is {} + {}?\n'.format(num1, num2)))
                break
            except:
                print('ERROR: this is not a number, try again')
        print(num1, num2, a, ask)
        if ask == a:
            self.correct += 1
            self.money += 1
            print('You have {} correct'.format(self.correct))
            print('You have {} money'.format(self.money))
        elif ask != a:
            self.wrong += 1
            self.money -= 10
            print('you lost 10 money, you now have {} money'.format(self.money))
            print('you got {} wrong so far'.format(self.wrong))
    
    def sub(self):
        num1, num2, a = game_extras.sub(self.max, self.min, self.neg)
        while True:
            try:
                ask = int(input('What is {} - {}?\n'.format(num1, num2)))
                break
            except:
                print('ERROR: this is not a number, try again')
        print(num1, num2, a, ask)
        if ask == a:
            self.correct += 1
            self.money += 7.5
            print('You have {} correct'.format(self.correct))
            print('You have {} money'.format(self.money))
        elif ask != a:
            self.wrong += 1
            self.money -= 7.5
            print('you lost 7.5 money, you now have {} money'.format(self.money))
            print('you got {} wrong so far'.format(self.wrong))
    
    def multi(self):
        num1, num2, a = game_extras.multi(self.max, self.min)
        while True:
            try:
                ask = int(input('What is {} * {}?\n'.format(num1, num2)))
                break
            except:
                print('ERROR: this is not a number, try again')
        print(num1, num2, a, ask)
        if ask == a:
            self.correct += 1
            self.money += 5
            print('You have {} correct'.format(self.correct))
            print('You have {} money'.format(self.money))
        elif ask != a:
            self.wrong += 1
            self.money -= 5
            print('you lost 5 money, you now have {} money'.format(self.money))
            print('you got {} wrong so far'.format(self.wrong))
    
    def div(self):
        num1, num2, a = game_extras.div(self.max, self.min, self.neg)
        while True:
            try:
                ask = int(input('What is {} / {}?\n'.format(num1, num2)))
                break
            except:
                print('ERROR: this is not a number, try again')
        print(num1, num2, a, ask)
        if ask == a:
            self.correct += 1
            self.money += 2.5
            print('You have {} correct'.format(self.correct))
            print('You have {} money'.format(self.money))
        elif ask != a:
            self.wrong += 1
            self.money -= 2.5
            print('you lost 2.5 money, you now have {} money'.format(self.money))
            print('you got {} wrong so far'.format(self.wrong))
    
    def over(self):
        print('GAME OVER')
        print('Wrong:\t{}'.format(self.wrong))
        print('Correct:\t{}'.format(self.correct))
        print('Money:\t{}'.format(self.money))

game = Game()