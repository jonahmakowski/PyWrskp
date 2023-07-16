from random import randint as r

def random_number(ma, mi):
    num = r(ma, mi)
    return num

def random_person(people_list):
    num = random_number(0, len(people_list)-1)
    return people_list[num]

def two_random_teams(people_list):
    team1 = []
    team2 = []
    while len(people_list) > 1:
        num = random_number(0, len(people_list) - 1)
        person = people_list[num]
        team1.append(person)
        del people_list[num]
        
        num = random_number(0, len(people_list) - 1)
        person = people_list[num]
        team2.append(person)
        del people_list[num]
    
    if len(people_list) == 1:
        team1.append(people_list[0])
    
    return team1, team2

if __name__ == '__main__':
    print(random_number(1,10))
    print(random_person(['Jonah', 'Lola', 'Mama', 'Papa', 'Noah']))
print(two_random_teams(['Jonah', 'Lola', 'Mama', 'Papa', 'Noah']))