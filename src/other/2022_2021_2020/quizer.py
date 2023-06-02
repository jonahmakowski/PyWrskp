from random import randint as r
from time import sleep as s


class Quiz:
    def __init__(self):
        self. a = [{'w': 'Scavengers', 'd': 'an animal or other organism that feeds on dead organic matter.'},
                {'w': 'Photosynthesis', 'd': 'the complex process by which carbon dioxide, water, and certain inorganic salts are converted into carbohydrates by green plants, algae, and certain bacteria, using energy from the sun and chlorophyll.'},
                {'w': 'Detritivores', 'd': 'an organism that uses organic waste as a food source, as certain insects.'},
                {'w': 'Tertiary consumers', 'd': 'a carnivore at the topmost level in a food chain that feeds on other carnivores; an animal that feeds only on secondary consumers.'},
                {'w': 'Ecosystem', 'd': 'a system, or a group of interconnected elements, formed by the interaction of a community of organisms with their environment'},
                {'w': 'Biome', 'd': 'a complex biotic community characterized by distinctive plant and animal species and maintained under the climatic conditions of the region, especially such a community that has developed to climax.'},
                {'w': 'Population', 'd': 'the assemblage of a specific type of organism living in a given area OR all the individuals of one species in a given area.'},
                {'w': 'Primary Consumers', 'd': 'an animal that feeds on plants; a herbivore.'},
                {'w': 'Decomposers', 'd': 'an organism, usually a bacterium or fungus, that breaks down the cells of dead plants and animals into simpler substances.'},
                {'w': 'Community', 'd': 'an assemblage of interacting populations occupying a given area.'},
                {'w': 'Producers', 'd': 'an organism, as a plant, that is able to produce its own food from inorganic substances.'},
                {'w': 'Secondary Consumers', 'd': 'a carnivore that feeds only on herbivores.'}]
        self.correct = 0
        self.wrong = 0

    def print_words(self):
        print('\n\nWORDS')
        printed = ['']
        for item in self.a:
            countinue = False
            while True:
                ra = r(0, len(self.a) - 1)
                for i in printed:
                    if self.a[ra] == i:
                        countinue = True
                if not countinue:
                    print(self.a[ra]['w'])
                    printed.append(self.a[ra])
                    break

        print('\n\nDEFINITIONS')
        printed = ['']
        for item in self.a:
            countinue = True
            while True:
                ra = r(0, len(self.a) - 1)
                for i in printed:
                    if self.a[ra] == i:
                        countinue = True
                if not countinue:
                    print(self.a[ra]['d'])
                    printed.append(self.a[ra])
                    break

    def vocab_quiz(self):
        i = 1
        while len(self.a) != 0:
            self.print_words()
            s(2)
            if i == 1:
                ra = r(0, len(self.a) - 1)
                awnser = input('\n\nWhat is the definition of {}?\n'.format(self.a[ra]['w']))
                if awnser == self.a[ra]['d']:
                    self.correct += 1
                    print('correct')
                    print('you now have {} correct'.format(self.correct))
                    print('you have {} wrong'.format(self.wrong))
                if awnser != self.a[ra]['d']:
                    self.wrong += 1
                    print('wrong')
                    print('you have {} correct'.format(self.correct))
                    print('you now have {} wrong'.format(self.wrong))
                    print('the correct answer is {}'.format(self.a[ra]['d']))
                    s(2)
                del self.a[ra]
            elif i == 2:
                ra = r(0, len(self.a) - 1)
                awnser = input('\n\nWhat is this the definition of? {}\n'.format(self.a[ra]['d']))
                if awnser == self.a[ra]['w']:
                    self.correct += 1
                    print('correct')
                    print('you now have {} correct'.format(self.correct))
                    print('you have {} wrong'.format(self.wrong))
                if awnser != self.a[ra]['w']:
                    self.wrong += 1
                    print('wrong')
                    print('you have {} correct'.format(self.correct))
                    print('you now have {} wrong'.format(self.wrong))
                    print('the correct answer is {}'.format(self.a[ra]['w']))
                    s(2)
                del self.a[ra]

            s(3)

            if i == 1:
                i = 2
            else:
                i = 1


q = Quiz()
q.vocab_quiz()
