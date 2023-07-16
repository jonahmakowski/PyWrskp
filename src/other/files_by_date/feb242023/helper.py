import time
import random


class BordemFair:
    def __init__(self, people):
        self.people = people

    def fight(self, print_=True):
        averages = []
        for item in self.people:
            info = item.compile_info()
            a = info['intelligence']
            a += info['speed']
            a += info['strength']
            a = a / 3
            averages.append(a)
        maxs = -1000000000000
        mins = 1000000000000
        maxnum = 0
        minnum = 0
        for i in range(len(averages)):
            if averages[i] > maxs:
                maxs = averages[i]
                maxnum = i
            if averages[i] < mins:
                mins = averages[i]
                minnum = i
        
        winner = self.people[maxnum]
        loser = self.people[minnum]
        if print_:
            print('The winner is {}! with a average rating of {}!'.format(winner.name, maxs))
            print('The loser is {}! with a average rating of {}'.format(loser.name, mins))
        return winner, loser

    def info(self, print_=True):
        info = []
        for item in self.people:
            i = item.compile_info()
            info.append(i)
        if print_:
            for item in info:
                print('Name: {}'.format(item['name']))
                print('Intelligence: {}'.format(item['intelligence']))
                print('Speed: {}'.format(item['speed']))
                print('Strength: {}'.format(item['strength']))
                print('Age: {}'.format(item['age']))
                print('Size: {}'.format(item['size']))
                print('Other Info:')
                for i in item['other']:
                    print('\t{}'.format(i))
                print()
                print()
                print()
        return info


class Person:
    def __init__(self, intelligence, speed, strength, size, age, name):
        self.intelligence = intelligence
        self.speed = speed
        self.strength = strength
        self.age = age
        self.size = size
        self.name = name
        self.other_info = []

    def compile_info(self):
        info = {'intelligence': self.intelligence,
                'speed': self.speed,
                'strength': self.strength,
                'size': self.size,
                'age': self.age,
                'name': self.name,
                'other': self.other_info}
        return info

    def learn(self, amount):
        self.intelligence += int(amount)

    def dumbify(self, amount):
        self.intelligence -= int(amount)

    def speed_up(self, amount):
        self.speed += int(amount)

    def speed_down(self, amount):
        self.speed -= int(amount)

    def stronger(self, amount):
        self.strength += int(amount)

    def weaker(self, amount):
        self.strength -= int(amount)

    def age(self, amount):
        self.age += int(amount)


def growing(person):
    while True:
        wait_time = 1
        time.sleep(10 * wait_time)
        person.age += 1
        if random.randint(1, 2) == 1:
            person.intellegance += 1
        else:
            if random.randint(1, 2) == 1:
                person.intellegance -= 1
        time.sleep(5 * wait_time)
        if random.randint(1, 2) == 1:
            person.speed += 1
        else:
            if random.randint(1, 2) == 1:
                person.speed -= 1


def fighting(fair, printing):
    while True:
        time.sleep(3)
        fair.fight(print_=printing)
        if printing:
            print()
            print()
            print()
