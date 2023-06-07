from time import sleep
from random import randint
import os
import platform

rand_words = ['actor', 'angry', 'answer', 'ape', 'baby', 'backwards', 'banana', 'baseball', 'blood', 
              'captain', 'card', 'cat', 'chair', 'checkers', 'cheese', 'children', 'circle', 'coal', 
              'coffee', 'copper', 'cord', 'corner', 'cotton', 'cloud','daughter', 'door', 'drain', 'drug', 
              'ears', 'expert', 'fan', 'finger', 'force', 'front', 'garden', 'girls', 'glove', 'goal', 
              'goldfish', 'grandmother', 'group', 'hands', 'hearing', 'heaven', 'hockey', 'hole', 'honey', 
              'hope', 'ice', 'iron', 'jam', 'jellyfish', 'kick', 'kitchen', 'knee', 'leader', 
              'lizards', 'mail', 'market', 'melon', 'mint', 'mitten', 'mountain', 'name', 'nation', 
              'needle', 'nest', 'oatmeal', 'office', 'orange', 'pear', 'pets', 'picture', 'rake',
              'rest', 'river', 'rock', 'room', 'rub', 'sand', 'saucer', 'scarf', 'scissors', 'season',
              'seat', 'shark', 'side', 'siren', 'skate', 'space', 'spot', 'steam', 'stew', 'sticks',
              'stop', 'sugar', 'sunrise', 'surprise', 'table', 'talk', 'thread', 'tongue', 
              'toothbrush', 'turkey', 'unicorn', 'village', 'vision', 'wash', 'water', 'wool', 'worm', 
              'wrench', 'yellow']
chosen_words = []
remembered_words = []
num_words = 10
display_time = 3

for i in range(num_words):
    index = randint(0, len(rand_words)+1)
    chosen_words.append(rand_words[index])
    del rand_words[index]

for word in chosen_words:
    print('                                           ', end="\r")
    print(word, end="\r")
    sleep(display_time)

print('Hello cheater...', end="\r")
if platform.system() == 'Linux' or platform.system() == 'Darwin':
    os.system('clear')
else:
    os.system('cls')

print('Input the words you can remember')
for i in range(num_words):
    word = input()
    word.lower()
    if word == '':
        break
    remembered_words.append(word)

for d in range(num_words - i):
    remembered_words.append('')

correct_list = []
missed_list = []
madeup_list = []
for count in range(num_words):
    if chosen_words[count] in remembered_words:
        correct_list.append(chosen_words[count])
    if remembered_words[count] not in chosen_words and remembered_words[count] != '':
        madeup_list.append(remembered_words[count])
    if chosen_words[count] not in remembered_words:
        missed_list.append(chosen_words[count])

print('\nAll Chosen Words:', len(chosen_words))
print(*chosen_words, sep='\n')

print('\nCorrect:', len(correct_list))
print(*correct_list, sep='\n')

print('\nMissed:', len(missed_list))
print(*missed_list, sep='\n')

print('\nMade Up:', len(madeup_list))
print(*madeup_list, sep='\n')
