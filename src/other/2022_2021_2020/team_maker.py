"""
I know I have an older team maker, but I thought I would use what I have learned so far to make a brand new one!

Here it is:
"""

import os
from random import randint
import json

try:
    pyWrkspLoc = os.environ["PYWRKSP"]

except KeyError:
    pyWrkspLoc = os.environ["HOME"] + input('Since you do not have the PYWRSKP env var '
                                            '\nPlease enter the pwd for the pyWrskp repo not including the '
                                            '"home" section')


class TeamMaker:
    def __init__(self, loc, t=None, d=None, pr=True):
        self.name = loc + '/docs/txt-files/team_maker_save.txt'
        change_t = False
        if t is None:
            change_t = True
        while True:
            if change_t:
                t = self.ask_t()

            if t == '2 teams':
                self.two_teams()
                if pr:
                    self.show()
                break

            elif t == '4 teams':
                self.four_teams()
                if pr:
                    self.show()
                break

            elif t == 'partners':
                self.partners()
                if pr:
                    self.show()
                break

            elif t == '2 teams + captions':
                self.two_teams()
                self.chose_caption()
                if pr:
                    self.show()
                break

            elif t == '4 teams + captions':
                self.four_teams()
                self.chose_caption()
                if pr:
                    self.show()
                break

            elif t == 'partners + captions':
                self.partners()
                self.chose_caption()
                if pr:
                    self.show()
                break

            else:
                if change_t is False:
                    print("As this option can't be changed, ending program")
                    exit()
                print('This value is not allowed, please try again')
                print('The options are:')
                print('"2 teams"')
                print('"4 teams"')
                print('"partners"')
                print('or if you add "+ captions" to any of them you will get one caption per team')
                print('asking again\n\n')

        if d is None:
            d = self.ask_l()

        self.d = d
        self.teams = []

    def ask_t(self):
        t = input('What type would you like?\n')
        return t

    def ask_l(self):
        d = []
        load = input('would you like to load the list? (y/n)')
        if load == 'n':
            print("Enter a list of the people's names if nothing is entered, the list will stop, you must include "
                  "more than one name")
            while True:
                l_add = input('')
                if l_add == '':
                    if len(d) != 1:
                        break
                elif l_add != '':
                    d.append(l_add)
            save = input('would you like to save this list? (y/n)')
            if save == 'y':
                self.save_list(d)

        elif load == 'y':
            d = self.load()

        else:
            print('{} is an word/char that this code does not allow'.format(load))
            exit(404)

        return d

    def two_teams(self):
        team_1 = []
        team_2 = []
        while len(self.d) > 1:
            person1 = randint(0, len(self.d) - 1)
            team_1.append(self.d[person1])
            del self.d[person1]
            person2 = randint(0, len(self.d) - 1)
            team_2.append(self.d[person2])
            del self.d[person2]

        if len(self.d) == 1:
            print('you have and uneven amount, adding {} to team 1'.format(self.d[0]))
            team_1.append(self.d[0])

        self.teams.append(team_1)
        self.teams.append(team_2)

    def four_teams(self):
        team_1 = []
        team_2 = []
        team_3 = []
        team_4 = []
        while len(self.d) > 3:
            person1 = randint(0, len(self.d) - 1)
            team_1.append(self.d[person1])
            del self.d[person1]

            person2 = randint(0, len(self.d) - 1)
            team_2.append(self.d[person2])
            del self.d[person2]

            person3 = randint(0, len(self.d) - 1)
            team_3.append(self.d[person3])
            del self.d[person3]

            person4 = randint(0, len(self.d) - 1)
            team_4.append(self.d[person4])
            del self.d[person4]

        if len(self.d) == 1:
            team_1.append(self.d[0])

        elif len(self.d) == 2:
            team_1.append(self.d[0])
            team_2.append(self.d[1])

        elif len(self.d) == 3:
            team_1.append(self.d[0])
            team_2.append(self.d[1])
            team_3.append(self.d[2])

        self.teams.append(team_1)
        self.teams.append(team_2)
        self.teams.append(team_3)
        self.teams.append(team_4)

    def partners(self):
        while len(self.d) >= 2:
            person1 = randint(0, len(self.d) - 1)
            person_1_name = self.d[person1]
            del self.d[person1]

            person2 = randint(0, len(self.d) - 1)
            person_2_name = self.d[person2]
            del self.d[person2]

            self.teams.append([person_1_name, person_2_name])

        if len(self.d) == 1:
            print('You have an uneven amount of people')
            print('I am making a group of three')
            self.teams[0].append(self.d[0])

    def chose_caption(self):
        for item in self.teams:
            caption_num = randint(0, len(item) - 1)
            caption_name = item[caption_num]
            del item[caption_num]
            item.append(caption_name + ' is Caption of the team')

    def load(self):
        try:
            with open(self.name) as json_file:
                j = json.load(json_file)
        except FileNotFoundError:
            print('This file, where the save is does not exist, to use this program make a file at {}.'
                  .format(self.name))
            exit(5)
        return j

    def save_list(self, d):
        with open(self.name, 'w') as outfile:
            json.dump(d, outfile)

    def show(self):
        team_num = 1
        for item_large in self.teams:
            print('Team {}'.format(team_num))
            for item in item_large:
                print(item)
            print('\n')
            team_num += 1


if __name__ == "__main__":
    teams = TeamMaker(pyWrkspLoc)
