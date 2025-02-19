import time
from datetime import date
import turtle
today = date.today()
today == date.fromtimestamp(time.time())
month = int(input('what is the month of your birthday?\nJanuary is 1, February is 2, March is 3, April is 4, May is 5, June is 6, July is 7, August is 8, September is 9, October is 10, November is 11, and December is 12\n'))
my_birthday = date(today.year, month, int(input('what is the day of your birthday?\n')))
time_to_birthday = abs(my_birthday - today)

days = turtle.Turtle()

setup = turtle.Turtle()
setup.penup()
setup.goto(-100, -20)

months = turtle.Turtle()
months.penup()
months.goto(0, 20)
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while True:
    today = date.today()
    today == date.fromtimestamp(time.time())
    days_in = days_in_month[today.month]
    if my_birthday < today:
         my_birthday = my_birthday.replace(year=today.year + 1)
    time_to_birthday = abs(my_birthday - today)
    time_to_birthday_2 = time_to_birthday.days / days_in
    time_to_birthday_2 = int(time_to_birthday_2)
    if time_to_birthday_2 * days_in != time_to_birthday:
        time_to_birthday_2 = (str(time_to_birthday_2) + ' months and ' + str(int(time_to_birthday.days) - (time_to_birthday_2 * days_in)) + ' days')
    months.write(time_to_birthday_2)
    days.write(str(time_to_birthday.days) + ' days')
    continue_q = ('are you done?')
    setup.write('please type in y/n for the following question (you must do this in the shell) ' + continue_q)
    continue_ = input(continue_q + ' (y/n)  ')
    if continue_ == 'y':
        break
    months.clear()
    days.clear()
print('SHUTTING DOWN')
time.sleep(3)