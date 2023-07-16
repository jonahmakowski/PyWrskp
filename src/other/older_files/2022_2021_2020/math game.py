money = 0
streak = 0
number_correct = 0
correct = 0
#import os
while True:
    try:
        ma = int(input('what would you like the largest number possible to be?\n'))
    except:
        pass
    
    if ma < 10:
        print('The largest possible number must be 10 or greater')
    else:
        break

def question(num1, num2, typ):
    if typ == '*':
        q = 'What is {} * {}?\n'.format(num1, num2)
        a = num1 * num2
    elif typ == '/':
        if num2 > num1:
            num2, num1 = num1, num2
        q = 'What is {} / {}?\n'.format(num1, num2)
        a = num1 / num2
    elif typ == '+':
        q = 'What is {} + {}?\n'.format(num1, num2)
        a = num1 + num2
    elif typ == '-':
        if num2 > num1:
            num2, num1 = num1, num2
        q = 'What is {} - {}?\n'.format(num1, num2)
        a = num1 - num2
    while True:
        an = input(q)
        try:
            an = float(an)
            break
        except:
            pass
    if an == a:
        return True
    elif an == False:
        return False
    else:
        print('The correct A is {}'.format(a))
        return False

def money_adding(addby, removeby, question, money):
    global streak
    global number_correct
    global correct
    if question == True:
        money += addby
        streak += 1
        number_correct += 1
        correct += 1
    else:
        money -= removeby
        streak = 0
        correct -= 1
    print('You have ${}!'.format(money))
    print('You have a streak of {}'.format(streak))
    print('You have gotten {} correct'.format(number_correct))
    return money

from random import randint as rand
addby = 10
removeby = 5
while True:
    #os.system("clear")
    TERM = True
    num = rand(1,4)
    num1 = rand(1,ma)
    num2 = rand(1,ma)
    
    if num == 1:
        q = question(num1, num2, '*')
        money = money_adding(addby, removeby, q, money)
    elif num == 2:
        q = question(num1, num2, '/')
        money = money_adding(addby, removeby, q, money)
    elif num == 3:
        q = question(num1, num2, '+')
        money = money_adding(addby, removeby, q, money)
    elif num == 4:
        q = question(num1, num2, '-')
        money = money_adding(addby, removeby, q, money)
    if correct == -10:
        print('you have gotten 10 wrong in a row, would you like to stop? (y/n)')
        stop = input('')
        if stop == 'y':
            break
        else:
            correct = 0
print('You have ${}!'.format(money))
print('You have a streak of {}'.format(streak))
print('You have gotten {} correct'.format(number_correct))
print('Thank you for playing!')
