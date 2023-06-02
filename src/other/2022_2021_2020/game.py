from time import sleep


class Game:
    def __init__(self, debug=False, health=200, cheat=True):
        self.number = 1
        self.number_killed = 1
        self.health = health
        self.attacks = [{'name':'blast', 'damage min':1, 'damage max':20},
                        {'name':'punch', 'damage min':5, 'damage max':10},
                        {'name':'super blast', 'damage min':-100, 'damage max':100}]
        self.debug = debug
        self.name = input('What is your name?\n')
        
        if cheat == True and self.name == 'Jonah':
            self.health = health * 10
            self.attacks.append({'name':'total destruction', 'damage min':999999999999998, 'damage max':999999999999999})
            for item in self.attacks:
                if item['damage min'] > 0:
                    item['damage min'] = item['damage min'] * 10
                if item['damage min'] < 0:
                    item['damage min'] = item['damage max'] - 1
                if item['damage max'] > 0:
                    item['damage max'] = item['damage max'] * 10
        
        if cheat == True and self.name == 'Noah':
            self.health = health * 3
            for item in self.attacks:
                if item['damage min'] > 0:
                    item['damage min'] = item['damage min'] * 3
                if item['damage min'] < 0:
                    item['damage min'] = item['damage max'] - 1
                if item['damage max'] > 0:
                    item['damage max'] = item['damage max'] * 3
                
            if self.debug:
                print('debug info: self.name == Jonah, so cheat mode has been enabled')
        
        self.print_info()
        
        if self.debug:
            print('debug info: self.print_info, done')
        
        sleep(2)
        while True:
            self.choose_bad()
            
            if self.debug:
                print('debug info: self.choose_bad, done \nnum {}'.format(self.number))
                
            self.number += 1
    
    def print_info(self):
        print('Hello {}!'.format(self.name))
        print('You have {} health'.format(self.health))
        print('Weapons you can use:')
        for item in self.attacks:
            name = item['name']
            name = name.upper()
            print('\t{} ({} - {} damage)'.format(name, item['damage min'], item['damage max']))
        print('Bad Guys:')
        print('\tGLOP - 10-20 attack damage - 50 health')
        print('\tBlock - 50 attack damage - 20 health')
        print('\tRANDOM KILLER - UNKNOWN - UNKOWN')
    
    def choose_bad(self):
        from random import randint
        
        num = randint(1,3)
        if self.debug:
            print('debug info: num in self.choose_bad is {}'.format(num))
        if num == 1:
            #self.glop()
            self.monster('glop', 20, 30, 50)
            self.number_killed += 1
        elif num == 2:
            self.monster('block', 50, 50, 20)
            self.number_killed += 1
        elif num == 3:
            self.monster('RANDOM KILLER', randint(1, 100), randint(100, 200), randint(100, 200))
        elif self.debug:
            print('debug info: issue, code could not find nums nessary\nsection: self.choose_bad')
        print('\n')
    
    def monster(self, name, attack_max, attack_min, monster_health):
        from random import randint
        monster_health = 50
        print('you meet a {}!'.format(name))
        while monster_health > 0 and self.health > 0:
            skip = False
            attack = input('What attack do you use {}? \n'.format(self.name))
            attack = attack.lower()
            if self.debug:
                print('debug info: attack input = {}'.format(attack))
            for item in self.attacks:
                if item['name'] == attack:
                    attack_dic = item
                    break
                else:
                    attack_dic = False
            if attack_dic == False:
                print('{} is not an attack name'.format(attack))
                print('Printing info again:')
                print('\n')
                self.print_info()
                skip = True
            
            if not skip:
                damage = randint(attack_dic['damage min'], attack_dic['damage max'])
                print('The {} lost {} health'.format(name, damage))
                monster_health -= damage
                print('The {} now has {} health'.format(name, monster_health))
                if monster_health > 0:
                    if attack_min == attack_max:
                        damage = attack_max
                    else:
                        damage = randint(attack_min, attack_max)
                    print('The {} did {} damage'.format(name, damage))
                    self.health -= damage
                    print('You now have {} health'.format(self.health))
        if self.health <= 0:
            print('you died!')
            print('GAME OVER')
            print('You killed {} bad guys'.format(self.number_killed))
            exit()
        else:
            print('GOOD JOB!')
            print('You killed the {} with {} health to spare!'.format(name, self.health))
            print('You killed {} bad guys so far'.format(self.number_killed))

    
User = Game(jonah=False) # add debug = True for debug info
