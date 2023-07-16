class FunStuff:
    def __init__(self):
        self.info = {}
    
    def collect_info(self):
        first_name = input('What is your first name?')
        last_name = input('What is your last name?')
        age = int(input('How old are you?'))
        gender = input('What gender are you?')
        house_country = input('What country do you live in?')
        house_province = input('What province/state do you live in?')
        house_city = input('What city do you live in?')
        house_street = input('What street do you live on?')
        house_number = input('What is your house number?')
        has_pet = input('do you have a pet? (y/n)')
        
        if has_pet == 'y':
            pet_type = input('What type of pet do you have? (cat, dog, fish, etc)')
            pet_name = input("What is your pet's name?")
            has_pet = True
        else:
            pet_type = 'NO PET'
            pet_name = 'NO PET'
            has_pet = False
        
        
        self.info = {'name': {'first': first_name, 'last': last_name},
                     'age': age,
                     'gender': gender,
                     'address': {'country': house_country, 'city': house_city, 'street': house_street, 'number': house_number, 'province': house_province},
                     'pet': {'has_pet': has_pet, 'type': pet_type, 'name': pet_name}}
    
    def tell_info(self):
        print('Your name is: {} {}'.format(self.info['name']['first'],
                                           self.info['name']['last']))
        
        print('You are {} years old'.format(self.info['age']))
        
        print('Your gender is {}'.format(self.info['gender']))
        
        print('Your address is {} {} {} {} {}'.format(self.info['address']['number'],
                                                      self.info['address']['street'],
                                                      self.info['address']['city'],
                                                      self.info['address']['province'],
                                                      self.info['address']['country']))
        
        if self.info['pet']['has_pet']:
            print('you have pet')
            
            print('The pet is called {}'.format(self.info['pet']['name']))
            
            print('He/She is a {}'.format(self.info['pet']['type']))
        else:
            print("You don't have a pet")
            
            print("You should get one though")

if __name__ == '__main__':
    fun = FunStuff()
    fun.collect_info()
    fun.tell_info()
