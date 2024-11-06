from random import randint as r
import classroom_tools_extras
import sys
sys.path.append('../notes')
import notes


class Classroom:
    def __init__(self):
        self.roster = []
        self.teacher = ''
        self.princaple = ''
        self.school_name = ''
        self.add_roster()

    def add_roster(self):
        print('Enter all of the students names:')
        while True:
            name = input('')
            if name == '':
                break
            self.roster.append(name)

    def team_maker(self):
        num_of_teams = input('How many teams would you like?')
        teams = []
        for i in range(int(num_of_teams)):
            teams.append([])
        roster_copy = self.roster
        
        while len(roster_copy) >= int(num_of_teams):
            for item in teams:
                person_num = r(0, len(roster_copy) - 1)
                person_name = roster_copy[person_num]
                del roster_copy[person_num]
                item.append(person_name)
        
        if len(roster_copy) > 0:
            i = 0
            while len(roster_copy) > 0:
                teams[i].append(roster_copy[0])
                del roster_copy[0]
                i += 1
        
        team_num = 0
        for item in range(len(teams)):
            print('Team {}'.format(team_num + 1))
            for i in range(len(teams[team_num])):
                print(teams[team_num][i])
            team_num += 1
            print('\n\n')

    def math_game(self):
        ty = input('What type of game would you like?')
        if ty == 'normal':
            classroom_tools_extras.basic_math_game()
        elif ty == 'challange':
            classroom_tools_extras.challange_math_game(self.roster)
    
    def classroom_log(self):
        log = notes.Notes(name='log.jonahtext')
        log.print_notes()
        add = input('would you like to add a note? (y/n/c)')
        if add == 'y':
            info = input('what is your note?')
            log.add_note(info)
            log.save_notes()
            print('your note, "{}" has been added to your saved notes!'.format(info))
        elif add == 'c':
            log.clear()


testing_class = Classroom()
do = input('What do you want to do?')
if do == 'team maker':
    testing_class.team_maker()
elif do == 'math game':
    testing_class.math_game()
elif do == 'classroom log':
    testing_class.classroom_log()
    