import time
from random import randint as r

lis = ['Imran',
       'Janine',
       'Tyem',
       'Lucas',
       'Sia',
       'Yagya',
       'Russell',
       'Lexie',
       'Catherine',
       'Melody',
       'Aranyo',
       'Mithru',
       'William',
       'Zihan',
       'Arjun',
       'Leah',
       'Sarim',
       'Charlotte',
       'Derek',
       'Joe',
       'Kevin',
       'Jonah']
current_num = r(0, len(lis) - 1)
current_name = str(lis[current_num])
print('THE LUCKY WINNER IS: {}'.format(current_name.upper()))
