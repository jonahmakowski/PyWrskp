from datetime import datetime
from random import randint


class Human:
    def __init__(self, gender, first_name, last_name, birth_year):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        current_year = datetime.now().year
        self.age = current_year - birth_year
    
    def talk(self, text):
        print('{} {}: {}'.format(self.first_name, self.last_name, text))
    
    def good_thing(self):
        options = ['Lola is the best',
                   'I had PE at school today',
                   'I played Roblox with my friends today',
                   'We went sledding',
                   'I had fun with my students today',
                   'We went to Bronte today']
        rad = randint(0, len(options) - 1)
        txt = 'Good thing: {}'.format(options[rad])
        self.talk(txt)
    
    def bad_thing(self):
        options = ['We went to Bronte today',
                   'I had to wake up at 6:00 am today for swimming']
        rad = randint(0, len(options) - 1)
        txt = 'Bad thing: {}'.format(options[rad])
        self.talk(txt)

Jonah = Human('male', 'Jonah', 'Makowski', 2010)
Noah = Human('male', 'Noah', 'Makowski', 2013)
Papa = Human('male', 'Maciej', 'Makowski', 1980)
Mama = Human('female', 'Karolina', 'Werner', 1979)

class Family:
    def __init__(self, members=[]):
        self.members = members
    def add(self, person):
        self.members.append(person)
    def good_thing_bad_thing(self):
        for i in range(len(self.members)):
            self.members[i].good_thing()
            print('\n')
            self.members[i].bad_thing()
            print('\n\n')

our_family = Family(members=[Jonah, Noah, Papa, Mama])

class House:
    def __init__(self, family, address_num, address_road, address_extenstion, address_city, address_province, address_country):
        self.family = family
        self.address_str = '{} {} {}, {}, {}, {}'.format(address_num, address_road, address_extenstion, address_city, address_province, address_country)
        self.address_dic = {'num': address_num,
                            'road': address_road,
                            'road type': address_extenstion,
                            'city': address_city,
                            'province': address_province,
                            'country': address_country}
    def day_or_night(self):
        now_hour = int(datetime.now().hour)
        if now_hour >= 20:
            print('night')
        else:
            print('day')

oakville = House(our_family, 449, 'Valley', 'Dr', 'Oakville', 'Ontario', 'Canada')
oakville.day_or_night()