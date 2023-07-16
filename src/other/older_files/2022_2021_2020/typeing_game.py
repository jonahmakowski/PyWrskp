from random import randint

class Typeing:
    def __init__(self):
        self.abcs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8',
                     '9', '0', '.', ',', '!', '?', ' ', ' ']
        self.current_string = ''
        self.wrong = 0
        self.typeing()
    
    def find_string(self):
        self.current_string = ''
        length = randint(5,20)
        for i in range(length):
            abc_item = randint(0, len(self.abcs) - 1)
            string = self.abcs[abc_item]
            self.current_string += string
    
    def typeing(self):
        print('Press enter to start the game!')
        input()
        print('Type the set of letters and/or numbers that are shown')
        print('Press enter to continue.')
        input()
        while True:
            self.find_string()
            inp = input(self.current_string + '\n')
            if not inp == self.current_string:
                print('That is incorrect!')
                self.wrong += 1
                print('You now have gotten {} wrong'.format(self.wrong))
                print('Press enter to countinue')
                input()

t = Typeing()
