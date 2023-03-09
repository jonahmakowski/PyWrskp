from random import randint


class FrenchAssignment:
    def __init__(self, user):
        self.user = user
        self.score = 0
    def trivia(self):
        questions = [{'question': 'Qui a chanté Sur Va Yeke?', 'awnser': 'Black M'},
                     {'question': 'Qui a chanté Outété?', 'awnser': 'KeenV'},
                     {'question': 'combien de temps dure Outété? (en une minute:seconde)', 'awnser': '4:29'}]
        print('BIENVENUE AU JEU-QUESTIONNAIRE!')
        while len(questions) > 1:
            q, questions = self.choose_random(questions, 1)
            print(q[0]['question'])
            awn = input('')
            awn = awn.lower()
            if awn == q[0]['awnser'].lower():
                print('Good Job, You are correct')
                self.score += 1
                print('Your current score is {}'.format(self.score))
            else:
                print('incorrect!')
                print('Your current score is {}'.format(self.score))
    
    def choose_random(self, l, amount):
        if len(l) < amount:
            print('choose_random has encountered an error')
            return False
        li = l
        r = []
        for i in range(amount):
            index = randint(0, len(li) - 1)
            r.append(li[index])
            del li[index]
        return r, li


assign = FrenchAssignment(input('Nom d’utilisateur:\n'))
assign.trivia()
