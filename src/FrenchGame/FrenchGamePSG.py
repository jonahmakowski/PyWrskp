from random import randint
import time
import webbrowser
import PySimpleGUI as psg


class FrenchAssignment:
    def __init__(self, user):
        self.user = user
        self.score = 0

    def trivia(self):
        questions = [{'question': 'Qui a chanté Sur Va Yeke?', 'awnser': 'Black M'},
                     {'question': 'Qui a chanté Outété?', 'awnser': 'KeenV'},
                     {'question': 'Combien de temps dure Outété? (en format minute:seconde)', 'awnser': '4:29'},
                     {'question': 'Combien de temps dure Rifia? (en format minute:seconde)', 'awnser': '3:02'},
                     {'question': 'Qui a gagné le premier tour?', 'awnser': 'Outete'},
                     {'question': 'Qui a gagné la deuxième ronde?', 'awnser': 'Danser avec toi'},
                     {'question': 'Qui a gagné la troisième ronde?', 'awnser': 'Case Depart'},
                     {'question': 'Qui a gagné la quatrième ronde?', 'awnser': 'Demain ca ira'}]
        psg.popup_yes_no('BIENVENUE AU JEU-QUESTIONNAIRE {}!\n' +
                         'Quand il y a une question comme celle-ci: Combien de temps dure ____,' +
                         'le temps est pris de la vidéo youtube.\n' +
                         'Tous les awnsers sont sans accent.'.format(self.user.upper()),
                         title="Règles du jeu-questionnaire")
        while len(questions) > 1:
            q, questions = self.choose_random(questions, 1)
            if not q:
                break
            awn = self.popup(q[0]['question'], 'JEU-QUESTIONNAIRE')
            awn = awn.lower()
            if awn == q[0]['awnser'].lower():
                self.score += 1
                self.notification('Bon travail, vous avez raison!\nVotre note actuelle est {}'.format(self.score))
            else:
                self.notification('incorrect!\nVotre note actuelle est {}\nLe bon awnser est {}'.format(self.score, q[0]['awnser']))
        self.notification('Le jeu-questionnaire est terminé!\n' +
                          'Vous avez {} points!'.format(self.score))

    @staticmethod
    def choose_random(l, amount):
        if len(l) < amount:
            print('choose_random has encountered an error')
            return False, False
        li = l
        r = []
        for i in range(amount):
            index = randint(1, len(li))
            index -= 1
            r.append(li[index])
            del li[index]
        return r, li

    def extras(self):
        extras = [{'name': 'Jeu-questionnaire Python',
                   'description' : 'Un code python qui vous permet de jouer au trivia.',
                   'link': None,
                   'command': 'trivia'},
                  {'name': 'Remplissez les blancs !',
                   'description': 'Un jeu de type trivia, mais remplissez les blancs!',
                   'link': None,
                   'command': 'blanks'}]

        q, l = self.choose_random(extras, 1)
        print(q[0]['name'])
        print(q[0]['description'])
        if q[0]['link'] is not None:
            print('Lien:\n{}'.format(q[0]['link']))
            time.sleep(2)
            webbrowser.open(q[0]['link'])
        else:
            if q[0]['command'] == 'trivia':
                time.sleep(2)
                self.trivia()
            if q[0]['command'] == 'blanks':
                time.sleep(2)
                self.blanks()

    def blanks(self):
        score = 0
        print('Bienvenue pour remplir les espaces {}!'.format(self.user))
        word_bank = ['seize', 'Canada', 'Nassi', 'Outété']
        questions = [{'question': 'Il y a _____ chansons dans Manie.', 'awnser': 'seize'},
                     {'question': 'Missy D est de ______.', 'awnser': 'Canada'},
                     {'question': '_____ chanté Rifia', 'awnser': 'Nassi'},
                     {'question': "______ is KeenV's Song", 'awnser': 'Outété'}]
        while True:
            if len(questions) == 0:
                break
            print('Banque de mots:')
            for word in word_bank:
                print(word)
            rand, questions = self.choose_random(questions, 1)
            if not rand:
                break
            rand = rand[0]
            print(rand['question'])
            user_input = input()
            if str(user_input).lower() == str(rand['awnser']).lower():
                print('C’est exact!')
                score += 1
                for item in word_bank:
                    if item == rand['awnser']:
                        del item
                print('Votre note actuelle est {}.'.format(score))
            else:
                print('C’est faux!')
                print('Votre note actuelle est {}.'.format(score))
                for item in word_bank:
                    if item == rand['awnser']:
                        del item
                print('Le bon awnser est {}.'.format(rand['awnser']))
        print('Blancs remplis!')
        print('Le score est {}!'.format(score))

    @staticmethod
    def popup(question, title):
        return psg.popup_get_text(question, title=title)

    @staticmethod
    def notification(text):
        psg.popup_notify(text)


assign = FrenchAssignment(input('Nom d’utilisateur:\n'))
#assign.extras()
assign.trivia()
