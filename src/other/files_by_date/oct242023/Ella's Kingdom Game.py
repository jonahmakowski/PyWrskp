from random import randint
from time import sleep



class Kingdom:
    def __init__(self):
        self.money = randint(70, 100)
        self.people = randint(70, 100)
        self.happiness = randint(70, 100)
        self.resources = randint(70, 100)
        self.mainloop()
    
    def mainloop(self):
        print('Welome to manage your kingdom')
        print("Adapted from Ella's game")
        sleep(2)
        while True:
            choice = randint(1, 1)
            
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('People: {}'.format(self.people))
            print('Happiness: {}'.format(self.happiness))
            print('Money: {}'.format(self.money))
            print('Resources: {}'.format(self.resources))
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            
            print('Waiting for something to happen!')
            sleep(randint(10, 20))
            
            if (self.people <= 0 or self.happiness <= 0) or (self.money <= 0 or self.resources <= 0):
                print('You lost!')
                print('Game Over!')
                break
            
            if choice == 1:
                self.earthquake()
            
            if (self.people > 100 or self.happiness > 100) or (self.money > 100 or self.resources > 100):
                if self.people > 100:
                    self.people = 100
                if self.happiness > 100:
                    self.happiness = 100
                if self.money > 100:
                    self.money = 100
                if self.resources > 100:
                    self.resources = 100
    
    def earthquake(self):
        print('You lost a third of all reasources to an earthquake.')
        money_taken = int(self.money / 3)
        people_taken = int(self.people / 3)
        happiness_taken = int(self.happiness / 3)
        resources_taken = int(self.resources / 3)
        
        self.money -= money_taken
        self.people -= people_taken
        self.happiness -= happiness_taken
        self.resources -= resources_taken

k = Kingdom()
