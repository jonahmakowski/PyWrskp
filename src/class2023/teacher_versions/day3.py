'''
star = ' *'
space=' '
maxLines = 20



for line in range (1,maxLines+1): # lines =1,2,3,4
    print(space*(maxLines-line)+star*line)


    for spaces in range(maxLines-line):
        print(space,end='')
        
    for stars in range(line): 
        print(star,end='')
    print()
        







range(3)

for stars in range(2):
    print(star,end='')
print()

for stars in range(3):
    print(star,end='')
print()


for stars in range(4):
    print(star,end='')
print()


maxLines = 4        maxLines-line
                        Line       spaces     stars
                        ------------------------------- 
--- *                  1                 3             1
-- * *                 2                 2            2
- * * *                3                 1            3
 * * * *               4                0             4

int()


#compartors:
#   ==  equal to
#  > greater than
#  < less than
#  >=  greater than  OR equal to
# <= less than or equal to
#  !=  not equal to
#   10 <= n <= 50      n=10 thru 50

from  random import randint
#import random

secret= randint(0,100)
print(secret)

guess= secret
if guess == secret:
    print('great')
else:
    if guess > secret :
        print('too high')
    else:
        print('too low')
    
if guess == secret:
    print('great')
elif guess > secret :
    print('too high')
else:
    print('too low')


Let's play Guess my Number between 0-100
what is your name?  John
hello John, you have 4 guesses
guess #1 : 40
Too Low
guess # 2 : 60
Too High
guess #3  : 53
You are correct!

guess #4 : 55
The Secret number was 56


name = input( ' what is your name? ')
print('hello' ,name,' , you have 4 guesses')

'''
guess = input(' guess->')
guessInt= int(guess)

guessInt= int( input('guess# ') )

for i in range(10):
    print(i)
    if i==3:
        continue
    if i ==6:
        break
    print('john')




      
