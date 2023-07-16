class WaterGunFight:
    def __init___(self):
        self.boats = []
        self.team_1 = []
        self.team_2 = []
        self.add_boats()
        self.add_people()
    
    def add_boats(self):
        possible_boats = [{'name': 'Excursion', 'people_max': '5', 'people_min': '1', 'type': 'rowboat'},
                          {'name': 'Seahawk', 'people_max': '2', 'people_min': '1', 'type': 'rowboat'},
                          {'name': "Jonah's Nunu", 'people_max': '1', 'people_min': '1', 'type': 'kayak'},
                          {'name': "Noah's Nunu", 'people_max': '1', 'people_min': '1', 'type': 'kayak'},
                          {'name': "Papa's Nunu", 'people_max': '1', 'people_min': '1', 'type': 'kayak'}]
        for item in possible_boats:
            use = input('Can you use {}? (y/n)'.format(item['name']))
            if use == 'y':
                team = input('What team is this craft on? (team1/team2)')
                item['team'] = team
                self.boats.append(item)
    
    def add_people(self):
        print('Team 1')
        print('Enter your name:')
        while True:
            name = input()
            if name == '':
                break
            self.team_1.append(name)
        
        print('Team 2')
        print('Enter your name:')
        while True:
            name = input()
            if name == '':
                break
            self.team_2.append(name)

cottage = WaterGunFight()
