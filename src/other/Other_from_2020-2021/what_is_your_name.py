import sys
import os

try:
    pyWrkspLoc = os.environ["PYWRKSP"]

except KeyError:
    pyWrkspLoc = os.environ["HOME"] + input('Since you do not have the PYWRSKP env var '
                                            '\nPlease enter the pwd for the pyWrskp repo not including the '
                                            '"home" section')

class Name:
    def __init__(self, name, pyWrskp):
        self.name = name
        self.pyWrskp = pyWrskp
        self.fun_stuff()

    def hello_world(self):
        print('Hello World')
        print('Your name is {}!'.format(self.name))

    def lola_is_the_best(self):
        for i in range(999):
            print('Lola is the best')

    def name(self):
        sys.path.append(self.pyWrskp + '/src/game')
        from game import Game
        g = Game

    def fun_stuff(self):
        option = input('What do you want to do {}?'.format(self.name))
        if option == 'hello world':
            self.hello_world()

        elif option == 'lola is the best':
            self.lola_is_the_best()

        elif option == 'game':
            self.name()


n = Name('Jonah')
