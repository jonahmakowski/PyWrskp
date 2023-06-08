from time import sleep
from random import randint
from sys import stdout

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
display_time = 5

for i in range(num_words):
    index = randint(0, len(rand_words)-1)
    chosen_words.append(rand_words[index])
    del rand_words[index]

for word in chosen_words:
    stdout.write("\033[F")
    print('                                     ')
    stdout.write("\033[F")
    print('\n'*40)
    print(word, end='')
    sleep(display_time)

stdout.write("\033[F")
print('                                     ')
stdout.write("\033[F")
print('\n'*40)

print('Input the words you can remember')
while len(remembered_words) <= num_words:
    word = input()
    word = word.lower()
    if word == '':
        break
    word = word.split()
    for item in word:
        remembered_words.append(item)

correct_list = []
missed_list = chosen_words.copy()
madeup_list = []
for count in range(len(remembered_words)):
    if remembered_words[count] in chosen_words:
        if remembered_words[count] in missed_list:
            correct_list.append(remembered_words[count])
            missed_list.remove(remembered_words[count])
    else:
        madeup_list.append(remembered_words[count])

print('\nAll Chosen Words:', len(chosen_words))
print(*chosen_words, sep='\n')

print('\nCorrect:', len(correct_list))
print(*correct_list, sep='\n')

print('\nMissed:', len(missed_list))
print(*missed_list, sep='\n')

print('\nMade Up:', len(madeup_list))
print(*madeup_list, sep='\n')
