import json

class Person:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.annoying_percent = self.generate_annoying()
    
    def print_info(self):
        print('First Name: {}'.format(self.first_name))
        print('Last Name: {}'.format(self.last_name))
        print('Age: {}'.format(self.age))
        print('Gender: {}'.format(self.gender))
        print('Annoying percent rating: {}'.format(self.annoying_percent))
    
    def generate_annoying(self):
        if self.first_name == 'Noah' and self.last_name == 'Makowski':
            return 200
        elif self.first_name == 'Stella' and self.last_name == 'Butler':
            return 75
        elif self.first_name == 'Jack' and self.last_name == 'Butler':
            return 100
        elif self.first_name == 'Lola' and self.last_name == 'Werner':
            return -100000000000000000000000000000000000000000000000000
        elif self.first_name == 'Jonah' and self.last_name == 'Makowski':
            return 0
        else:
            return 'unkown'
    
    def save_info(self):
        try:
            with open('../../../docs/txt-files/people.txt') as json_file:
                info = json.load(json_file)
        except:
            info = []
        info.append({'first_name':self.first_name,
                     'last_name':self.last_name,
                     'age':self.age,
                     'gender':self.gender,
                     'annoying':self.annoying_percent})
        with open('../../../docs/txt-files/people.txt', 'w') as outfile:
            json.dump(info, outfile)
        
Jonah = Person('Jonah', 'Makowski', 12, 'male')        
Jonah.print_info()
Jonah.save_info()
