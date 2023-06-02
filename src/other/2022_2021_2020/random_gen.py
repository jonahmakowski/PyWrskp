from random import randint as r
from time import sleep as wait

# RANDOM GEN


class RandomGen:
    def __init__(self, version):
        self.lis = []
        if version == 'num':
            length = int(input('What do you want to range to be, 0 to'))
            self.lis = range(length)
            self.num()
            exit()
        elif version == 'names':
            print('Enter the names, nothing means end')
            while True:
                name = input()
                if name == '':
                    break
                self.lis.append(name)
            self.names()
    
    def num(self):
        current_num = r(0, len(self.lis))
        print('The number is {}'.format(current_num))
    
    def names(self):
        current_num = r(0, len(self.lis) - 1)
        current_name = str(self.lis[current_num])
        print('THE LUCKY WINNER IS: {}'.format(current_name.upper()))
        wait(5)
        print('Name was entered as {}'.format(current_name))
        

Random = RandomGen(input('What version'))
