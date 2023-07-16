a_or_b = input('would you like partners, three person groups, half and half, or one person?\n')

if a_or_b == ('partners'):
    from random import randint
    names = []
    while True:
        name = input('What name would you like to add?\n')
        if name == (''):
            break
        names.append(name)
    while len(names) >= 2:
        a = randint(0, len(names) - 1)
        b = names[a]
        del names[a]
        c = randint(0, len(names) - 1)
        d = names[c]
        del names[c]
        print(d + ' and ' + b + ' are working as a group!')
        input()
    if len(names) == 1:
        print('you have an uneven amount of people in your list so we could not find a partner for ' + names[0])
    print('those are all your names')
    exit()

if a_or_b == ('one person'):
    from random import randint
    names = []
    while True:
        name = input('What name would you like to add?\n')
        if name == (''):
            break
        names.append(name)
    while True:
        if len(names) == 0:
            break
        a = randint(0, len(names) - 1)
        print('The name that was chosen is ' + names[a] + '!')
        del names[a]
        input()
    print('Those are all your names!')
    exit()

if a_or_b == ('three person groups'):
    from random import randint
    names = []
    while True:
        name = input('What name would you like to add?\n')
        if name == (''):
            break
        names.append(name)
    while len(names) >= 3:
        a = randint(0, len(names) - 1)
        b = names[a]
        del names[a]
        c = randint(0, len(names) - 1)
        d = names[c]
        del names[c]
        e = randint(0, len(names) - 1)
        f = names[e]
        del names[e]
        print(d + ', ' + b + ' and ' + f + ' are working as a group!')
        input()
    if len(names) == 1:
        print('you have an uneven amount of people in your list so we could not find a group for ' + names[0])
    if len(names) == 2:
        print('you have an uneven amount of people in your list so we could not find a group for ' + names[0] + ' and ' + names[1])
    print('those are all your names')
    exit()
if a_or_b == ('half and half'):
    import time
    from random import randint
    names = []
    
    while True:
        name = input('What name would you like to add?\n')
        
        if name == (''):
            break
        else:
            names.append(name)
    
    half_float = len(names) / 2
    half_int = int(half_float)
    
    team_1 = []
    team_2 = []
    
    while len(names) >= 2:
        a = randint(0, len(names) - 1)
        team_1.append(names[a])
        del names[a]
        b = randint(0, len(names) - 1)
        team_2.append(names[b])
        del names[b]
    
    if half_float != float(half_int):
        team_1.append(names[0])
    print('Team 1')
    for i in range(len(team_1)):
        print(team_1[i])
        time.sleep(0.5)
    
    print('Team 2')
    for i in range(len(team_2)):
        print(team_2[i])
        time.sleep(0.5)
'''
if a_or_b == ('half and half (girls then boys)'):
    import time
    from random import randint
    boys = []
    girls = []
    print("please enter the girls' names")
    while True:
        name = input('')
        if name == (''):
            break
        else:
            girls.append(name)
    print("please enter the boys' names")
    while True:
        name = input('')
        if name == (''):
            break
        else:
            boys.append(name)
    team_1 = []
    team_2 = []
    while len(girls) >= 2:
        a = randint(0, len(girls) - 1)
        team_1.append(girls[a])
        del girls[a]
        a = randint(0, len(girls) - 1)
        team_2.append(girls[a])
        del girls[a]
    if len(girls) == 1:
        team_1.append(girls[0])
        del girls[0]
    while len(boys) >= 2:
        a = randint(0, len(boys) - 1)
        team_1.append(boys[a])
        del boys[a]
        a = randint(0, len(boys) - 1)
        team_2.append(boys[a])
        del boys[a]
    if len(boys) == 1:
        team_2.append(boys[0])
        del boys[0]
    print('Team 1')
    for i in range(len(team_1)):
        print(team_1[i])
        time.sleep(0.5)
    
    print('Team 2')
    for i in range(len(team_2)):
        print(team_2[i])
        time.sleep(0.5)
    print('That is it!')
'''
