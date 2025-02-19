# compute number of months and days from today to my next bday
import datetime
from dateutil import relativedelta

bday = datetime.date(2010, 5, 29)
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
    print('Next birthday is in ' + (str(n_months)) + ' months and ' + (str(n_days)) + ' days.')
pass
