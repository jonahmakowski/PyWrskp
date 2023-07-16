import time
from datetime import date

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    if my_birthday.year%4==0:
        days_in_month[1] = 29
    elif my_birthday.year%4!=0:
        days_in_month[1] = 28
    today = date.today()
    today = date.fromtimestamp(time.time())
    # today = today.replace(year=2024, month=2, day=28)
    month = int(input('what is the month of your birthday?\nJanuary is 1, February is 2, March is 3, April is 4, May is 5, June is 6, July is 7, August is 8, September is 9, October is 10, November is 11, and December is 12\n'))
    my_birthday = date(today.year, month, int(input('what is the day of your birthday?\n')))
    time_to_birthday = abs(my_birthday - today)
    days_in = days_in_month[today.month]
    time_to_birthday_2 = time_to_birthday.days / days_in
    time_to_birthday_2 = int(time_to_birthday_2)
    if my_birthday < today:
         my_birthday = my_birthday.replace(year=today.year + 1)
    if time_to_birthday_2 * days_in != time_to_birthday:
        time_to_birthday_2 = (str(time_to_birthday_2) + ' months and ' + str(int(time_to_birthday.days) - (time_to_birthday_2 * days_in)) + ' days')
    print(time_to_birthday_2)
    print('or')
    print(str(time_to_birthday.days) + ' days')
    continue_ = input('would you like a new bday? (y/n)\n')
    if continue_ == 'n':
        break
    print('reloading')
    time.sleep(1)
print('SHUTTING DOWN')
