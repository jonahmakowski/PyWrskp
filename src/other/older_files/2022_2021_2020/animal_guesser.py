import os
import json


try:
    pyWrkspLoc = os.environ["PYWRKSP"]

except KeyError:
    pyWrkspLoc = os.environ["HOME"] + input('Since you do not have the PYWRSKP env var '
                                            '\nPlease enter the pwd for the pyWrskp repo not including the '
                                            '"home" section')


class AnimalChoser:
    def __init__(self, pywrskp):
        self.name_1 = pywrskp + '/docs/txt-files/animal_chooser_options.txt'
        self.name_2 = pywrskp + '/docs/txt-files/animal_chooser_atturbites.txt'
        self.options = []
        self.atturbites = []
        self.load()
        self.correct_atturbites = []
        do = input('would you like to add or play?')
        if do == 'play':
            print('The current options for this game are:')
            for item in self.options:
                print(item['name'])
            self.guess()
        else:
            self.add()

    def guess(self):
        for item in self.atturbites:
            yes_or_no = input('is this animal/does it have {} (y/n)?'.format(item['name']))
            item['y/n'] = yes_or_no

        for item in self.atturbites:
            if item['y/n'] == 'y':
                self.correct_atturbites.append(item['name'])

        choosen = False

        for item in self.options:
            item['info'] = sorted(item['info'])

        self.correct_atturbites = sorted(self.correct_atturbites)

        for item in self.options:
            if item['info'] == self.correct_atturbites:
                print('your animal is {}'.format(item['name']))
                choosen = True
                break

        if not choosen:
            print("This program can figure out what you choose, make sure it is on this list:")
            for item in self.options:
                print(item['name'])

            '''print('debug info:')
            print('self.correct_atturbites:')
            print(self.correct_atturbites)
            print('self.options:')
            print(self.options)'''

    def load(self):
        try:
            with open(self.name_1) as json_file:
                self.options = json.load(json_file)
        except FileNotFoundError:
            print('This file does not exist (num1)')
            exit(5)

        try:
            with open(self.name_2) as json_file:
                self.atturbites = json.load(json_file)
        except FileNotFoundError:
            print('This file does not exist (num2)')
            exit(5)

    def add(self):
        new_name = input('What is the name of this animal?')
        new = {"name": new_name, "info": []}
        new_attrbs = []
        print('What are the atturbuites?')
        while True:
            attrb = input()
            if attrb == '':
                break
            new_attrbs.append(attrb)
            new["info"].append(attrb)

        for item in new_attrbs:
            for atra in self.atturbites:
                if item == atra:
                    del item

        for item in new_attrbs:
            self.atturbites.append({'name': item, "y/n": ""})

        self.options.append(new)

        with open(self.name_1, 'w') as outfile:
            json.dump(self.options, outfile)
        with open(self.name_2, 'w') as outfile:
            json.dump(self.atturbites, outfile)


game = AnimalChoser(pyWrkspLoc)
