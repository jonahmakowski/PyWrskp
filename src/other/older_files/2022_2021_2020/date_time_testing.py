import datetime
from dateutil import relativedelta

bday = datetime.date(2010, int(input('What month were you born in (numbers please)\n')), int(input('What day of the month were you born in (numbers please)\n')))
today = datetime.date.today()
age = today - bday
cur_yr = today.year
next_bday = bday.replace(year=cur_yr)
if next_bday < today:       # already passed this year, consider bday next year
    next_bday = next_bday.replace(year=cur_yr + 1)
diff = next_bday - today
diff2 = relativedelta.relativedelta(next_bday, today)
n_months = diff2.months
n_days = diff2.days
if n_months == 0 and n_days == 0:
    print('Your birthsday is TODAY.')
else:
    # print('Next birthday is in ' + (str(n_months)) + ' months and ' + (str(n_days)) + ' days.')
    import turtle
    import time
    t = turtle.Turtle()
    while True:
        diff2 = relativedelta.relativedelta(next_bday, today)
        n_months = diff2.months
        n_days = diff2.days
        t.write('your next birthday is in ' + (str(n_months)) + ' months and ' + (str(n_days)) + ' days.')
        time.sleep(86400) # wait one
        t.clear()
pass
