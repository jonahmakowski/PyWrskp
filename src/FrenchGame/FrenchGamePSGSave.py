from random import randint
import time
import webbrowser
import Helper


class FrenchAssignment:
    def __init__(self, user):
        self.user = user

    def trivia(self):
        current_high_score = Helper.read_file('high_scores_trivia.txt')
        questions = [{'question': 'Qui a chanté Sur Va Yeke?', 'awnser': 'Black M'},
                     {'question': 'Qui a chanté Outété?', 'awnser': 'KeenV'},
                     {'question': 'Combien de temps dure Outété? (en format minute:seconde)', 'awnser': '4:29'},
                     {'question': 'Combien de temps dure Rifia? (en format minute:seconde)', 'awnser': '3:02'},
                     {'question': 'Qui a gagné le premier tour?', 'awnser': 'Outete'},
                     {'question': 'Qui a gagné la deuxième ronde?', 'awnser': 'Danser avec toi'},
                     {'question': 'Qui a gagné la troisième ronde?', 'awnser': 'Case Depart'},
                     {'question': 'Qui a gagné la quatrième ronde?', 'awnser': 'Demain ca ira'}]
        Helper.show_window('BIENVENUE AU JEU-QUESTIONNAIRE {}!\n'.format(self.user.upper()) +
                           'Quand il y a une question comme celle-ci: Combien de temps dure ____,' +
                           'le temps est pris de la vidéo youtube.\n' +
                           'Tous les awnsers sont sans accent.\n' +
                           'L’utilisateur {} a le score actuel le plus élevé à {}!'.format(current_high_score['username'],
                                                                                           current_high_score['score']),
                           " du jeu-questionnaire")
        score = 0
        while len(questions) > 1:
            q, questions = self.choose_random(questions, 1)
            if not q:
                break
            awn = Helper.popup(q[0]['question'], 'JEU-QUESTIONNAIRE')
            if awn is not None:
                awn = awn.lower()
                if awn == q[0]['awnser'].lower():
                    score += 1
                    Helper.show_window('Bon travail, vous avez raison!\nVotre note actuelle est {}'.format(score),
                                       'Correct, bon travail!')
                else:
                    Helper.show_window('incorrect!\nVotre note actuelle est {}\nLe bon awnser est {}'.format(score, q[0]['awnser']),
                                       'incorrect')
            else:
                Helper.show_window('incorrect!\nVotre note actuelle est {}\nLe bon awnser est {}'.format(score, q[0]['awnser']),
                                   'incorrect')
        Helper.show_window('Le jeu-questionnaire est terminé!\n' +
                           'Vous avez {} points!'.format(score),
                           'Fin du jeu-questionnaire')
        current_high_score = Helper.read_file('high_scores_trivia.txt')
        set_score = True
        if score > current_high_score['score']:
            Helper.show_window('Vous avez battu le score actuel de {} (par {} points)!'
                               .format(current_high_score['score'], score - current_high_score['score']),
                               'Nouveau Score élevé')
        elif score < current_high_score['score']:
            Helper.show_window('Votre score est inférieur au score actuel. Si vous aviez {} plus de points, vous seriez égal au score élevé!'
                               .format(current_high_score['score'] - score), 'Moins que le score actuel.')
            set_score = False
        elif score == current_high_score['score']:
            Helper.show_window('Vous êtes égal au score élevé actuel! Puisque vous êtes plus récent, vous réclamez le nouveau score élevé.',
                               'Égal au score élevé')
            set_score = True
        if set_score:
            Helper.write_file('high_scores_trivia.txt', {'username': self.user, 'score': score})

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
        Helper.show_window(q[0]['name'] + '\n' + q[0]['description'], 'info')
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
        current_high_score = Helper.read_file('high_scores_blanks.txt')
        Helper.show_window('Bienvenue pour remplir les espaces {}!\nLe score actuel le plus élevé est {}!'
                           .format(self.user, current_high_score['score']),
                           'Règles')
        word_bank = ['Seize',
                     'Canada',
                     'Nassi',
                     'Outete',
                     '4:29']
        questions = [{'question': 'Il y a _____ chansons dans Manie.', 'awnser': 'Seize'},
                     {'question': 'Missy D est de ______.', 'awnser': 'Canada'},
                     {'question': '_____ chanté Rifia', 'awnser': 'Nassi'},
                     {'question': "______ is KeenV's Song", 'awnser': 'Outete'},
                     {'question': 'La chanson Outété est ____ longue. (en format minute/seconde)', 'awnser': '4:29'}]
        while True:
            if len(questions) == 0:
                break
            words_string = ''
            for word in word_bank:
                words_string += word + '\n'
            rand, questions = self.choose_random(questions, 1)
            if not rand:
                break
            rand = rand[0]
            user_input = Helper.popup('Banque de mots:\n' + words_string + '\n\n\n' + rand['question'], 'Entrée')
            if str(user_input).lower() == str(rand['awnser']).lower():
                score += 1
                Helper.show_window('C’est exact!\nVotre note actuelle est {}.'.format(score), 'Vrai')
            else:
                Helper.show_window('C’est faux!\nVotre note actuelle est {}.\nLe bon awnser est {}.'.format(score, rand['awnser']), 'Faux')
        Helper.show_window('Blancs remplis!\nLe score est {}!'.format(score), 'Blancs remplis!')
        current_high_score = Helper.read_file('high_scores_blanks.txt')
        if current_high_score['score'] >= score:
            Helper.show_window('Votre score est supérieur ou égal au score le plus élevé!\nBon travail!',
                               'nouveau score élevé.')
            Helper.write_file('high_scores_blanks.txt.txt', {'username': self.user, 'score': score})


assign = FrenchAssignment(Helper.popup('Nom d’utilisateur:', 'Nom d’utilisateur'))
assign.extras()
