class House:
    def __init__(self, family_members_list, pets_list):
        self.family = family_members_list
        self.pets = pets_list
    def new_family_member(self):
        pet = input('Are you adding a pet? (y/n)  ')
        if pet == 'y':
            name = input('What is the name of the pet?  ')
            self.pets.append(name)
        elif pet == 'n':
            name = input('What is the name of the person you want to add?  ')
            self.family.append(name)
        print(name + ' has been added')
    def show_family(self):
        print('Pet(s):')
        for pets in self.pets:
            print(pets)
        print('people:')
        for people in self.family:
            print(people)
    def food_ideas(self):
        from random import randint as r
        foods = ['Pad Thai', 'Salmon', 'Chicken Wings', 'Tomato Soup', 'Hamburgers', 'Steak', 'Bullgogi', 'eggs', 'home made pizza', 'Lasagna', 'sandwichs', 'Pancakes']
        while True:
            if len(foods) <= 0:
                print('those are all our ideas, sorry')
                break
            a = r(0, len(foods) - 1)
            print('your food plan for today is: ' + foods[a])
            del foods[a]
            not_working = input('Is this plan not working?\ndo you need a new idea? (y/n)  ')
            if not_working == 'n':
                break
    def what_to_do(self):
        ideas = ['go on a walk to pick up the mail', 'play on your device', 'watch a movie', 'go to a park']
        if len(self.pets) >= 1:
            ideas.append('take ' + pets[0] + ' on a walk')
        from random import randint as r
        while True:
            if len(ideas) <= 0:
                print('those are all our ideas, sorry')
                break
            a = r(0, len(ideas) - 1)
            print('you should: ' + ideas[a])
            not_working = input('Is this idea not working?\ndo you need a new idea? (y/n)  ')
            del ideas[a]
            if not_working == 'n':
                break
def new_house():
    humans = []
    pets = []
    print('enter the names of all the people')
    while True:
        human = input('')
        if human == (''):
             break
        else:
            humans.append(human)
        print('enter the names of all the pets')
        while True:
            pet = input('')
            if pet == (''):
                break
            else:
                pets.append(pet)
        house = House(humans, pets)
        return house
def extra():
    print('please create your house')
    house = new_house()
    houses = [house]
    i = 0

    while True:
        what_do = input('What would you like to do?   ')
        if what_do == ('add new family members'):
            houses[i].new_family_member()
        elif what_do == ('print family list'):
            houses[i].show_family()
        elif what_do == ('food ideas'):
            houses[i].food_ideas()
        elif what_do == ('what do'):
            houses[i].what_to_do()
        elif what_do == ('change house'):
            change = int(input('What number would you like to change to?  '))
            if change <= len(houses) - 1:
                i = change
            else:
                i = len(houses) - 1
                print('The valuse you entered is too high, you have been put at your possible value.')
                print('To create more house please enter "create new house" the next time the "What would you like to do?" question pops up')
        elif what_do == ('create new house'):
            house = new_house()
            houses.append(house)
        elif what_do == 'close':
            return
        else:
            print('That is not a option')
extra()