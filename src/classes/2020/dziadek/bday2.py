# compute number of months and days from today to my next bday
# import sys needed if sys.exit() used
import datetime
from dateutil import relativedelta


# handle and process the bday data
class NextBday:
    def __init__(self, b_month, b_day, b_yr=0, cheat_today=False):
        self.use_dateutl = True     # set to False, if dateutil not available
        try:
            assert not (b_month < 1 or b_month > 12)
        except AssertionError:
            print('Month number must be in [1, 12]. Provided value of ' + str(b_month) + ' is illegal.')
            # sys.exit('wrong month')
            raise
        try:
            # Note: this is incomplete check (one can e.g., specify Apr 31 or Feb 30)
            assert not(b_day < 1 or b_day > 31)
        except AssertionError:
            print('Day number must be in [1, 31]. Provided value of ' + str(b_day) + ' is illegal.')
            # sys.exit('wrong day')
            raise
        self.b_month = b_month
        self.b_day = b_day
        self.b_yr = b_yr      # optional bday-year; if defined then the age is calculated
        if cheat_today: # for testing: set below a date to be used as today's date
            cheated = datetime.date(2021, 5, 29)
            self.today = cheated
        else:
            self.today = datetime.date.today()
        self.cur_yr = self.today.year
        if b_yr:
            self.bday_defined = True
            self.birth = datetime.date(b_yr, b_month, b_day)
        else:
            self.bday_defined = False
            self.birth = datetime.date(self.cur_yr, b_month, b_day)
        self.next_bday = self.birth.replace(year=self.cur_yr)
        if self.next_bday < self.today:       # already passed this year, consider bday next year
            self.next_bday = self.next_bday.replace(year=self.cur_yr + 1)

    def bday_info(self):
        print('Today is: ' + str(self.today))
        if self.bday_defined:
            print('On ' + str(self.next_bday) + ' you will be ' + str(self.next_bday.year - self.birth.year) +
                  ' years old.')
        else:
            print('Your next birthday will be on: ' + str(self.next_bday))

    def bday_in(self):  # calculate and print number of months and days until next birthday
        if not self.use_dateutl:
            self.bday_in2()  # do the calculation without using dateutil
            return
        away = relativedelta.relativedelta(self.next_bday, self.today)
        n_months = away.months
        n_days = away.days
        if n_months == 0 and n_days == 0:
            print('Your birthsday is TODAY.')
        else:
            print('You have to wait ' + (str(n_months)) + ' months and ' + (str(n_days)) + ' days for your bday party.')

    # calculate and print number of months and days until next birthday without using datautil
    # place-holder for the code to be written by Jonas
    def bday_in2(self):
        print('bday_in2() not implemented yet')
        print('Number of months and days until ' + str(self.next_bday) + ' not available.')


# testing the NextBday class
bday = NextBday(3, 29, 1946)    # ctor with full bday (month, day, yr)
bday.bday_info()
bday.bday_in()
#
print('\nNext test:')
bday = NextBday(5, 29)    # ctor without the birth-year
bday.bday_info()
bday.bday_in()
#
print('\nNext test:')
bday = NextBday(5, 29, 2010, True)    # ctor for testing (uses the Today value specified in the ctor)
bday.bday_info()
bday.bday_in()
pass
