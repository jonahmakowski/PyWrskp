_4_5 = {'teacher':'Mr.Payne', 'students':['Ayaan', 'Nathaniel', 'Ethan', 'Kennedy', 'Shay', 'Dimitriana','Laith','Tamanna', 'Anna', 'Kaitlyn', 'Nathan', 'Jonah', 'Raleigh', 'Arijon', 'Jairus', 'Lauren', 'Abhijay', 'Liam', 'Lydia', 'Arionna', 'Calvin', 'Maxwell', 'Nyla']}

from random import randint

team_1 = []
team_2 = []
x = _4_5['students']
while len(x) >= 2:
    i = randint(0, len(x)-1)
    team_1.append(x[i])
    del x[i]
    i = randint(0, len(x)-1)
    team_2.append(x[i])
    del x[i]
if len(x) == 1:
    team_1.append(x[0])
caption = team_1[i]
del team_1[i]
i = randint(0, len(team_1)-1)
team_1 = {'team_caption':caption, 'members':team_1}
team_1_members = team_1['members']

i = randint(0, len(team_2)-1)
caption = team_2[i]
del team_2[i]
team_2 = {'team_caption':caption, 'members':team_2}
team_2_members = team_2['members']

print('teacher: ' + _4_5['teacher'])

print('\nteam 1:')
print('team caption: ' + team_1['team_caption'])
for person in team_1_members:
    print(person)

print('\nteam 2:')
print('team caption: ' + team_2['team_caption'])
for person in team_2_members:
    print(person)
