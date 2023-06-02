from random import randint as r
from time import sleep as s


class RockPaperScissors:
    def __init__(self):
        self.player_name = input('What is your name?\n')
        print('Welcome to Rock Paper Scissors!')

        self.cheat = 'n'

        if self.player_name == 'Jonah':
            self.cheat = input('would you like to cheat? (y/n)')

        self.computer_choice = ''
        self.player_choice = ''

        self.setup()

    def setup(self):
        print('This is how you play (& how the code works)')
        s(1)
        print('The computer will choose a option')
        s(1)
        print('You will chose an option')
        s(1)
        print('The computer will tell you who won')
        s(1)

        self.play()

    def play(self):
        self.computer_choose()
        self.player_choose()
        self.show_winner()

    def computer_choose(self):
        print('The computer is choosing...')
        random_number = r(1, 3)

        if random_number == 1:
            self.computer_choice = 'paper'
        elif random_number == 2:
            self.computer_choice = 'rock'
        elif random_number == 3:
            self.computer_choice = 'scissors'
        s(2)
        print('the computer has chosen')
        if self.cheat == 'y':
            print('The computer choose {}'.format(self.computer_choice))

    def player_choose(self):
        print('its you turn to choose, {}!'.format(self.player_name))
        s(2)

        while True:
            self.player_choice = input('What would you like to choose (paper, rock, scissors)?')
            if (self.player_choice == 'paper' or self.player_choice == 'rock') or self.player_choice == 'scissors':
                break
            else:
                print('That is not one of the three options, try again!')
                s(2)

    def show_winner(self):
        if ((self.player_choice == 'rock' and self.computer_choice == 'paper') or (self.player_choice == 'scissors' and self.computer_choice == 'rock')) or self.player_choice == 'paper' and self.computer_choice == 'scissors':
            print('You Lose')
            s(2)
            print('the computer choose {} and you choose {}'.format(self.computer_choice, self.player_choice))
        elif ((self.computer_choice == 'rock' and self.player_choice == 'paper') or (self.computer_choice == 'scissors' and self.player_choice == 'rock')) or self.computer_choice == 'paper' and self.player_choice == 'scissors':
            print('You win')
            s(2)
            print('the computer choose {} and you choose {}'.format(self.computer_choice, self.player_choice))
        elif self.computer_choice == self.player_choice:
            print('This is a tie, would you like to play again?')
            print('You both choose {}.'.format(self.computer_choice))
            again = input('y/n')
            if again == 'y':
                self.setup()
        else:
            print('The code failed to figure out who won')
            print('The computer choose {} and you choose {}'.format(self.computer_choice, self.player_choice))


play = RockPaperScissors()
