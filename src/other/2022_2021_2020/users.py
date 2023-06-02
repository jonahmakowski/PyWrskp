from datetime import date
class Human:
    def __init__(self, fname, lname, age, tec_age=False, _ = None):
        self.shut_off = False
        self.pin = 1982
        self.today = date.today()
        if tec_age == True:
            if _ == '+':
                tec_age = age + 1
            if _ == '-':
                tec_age = age - 1
        else:
            tec_age = age
        self.info = {'name':{'first name':fname,'last name':lname},
                     'age':{'str':str(age),'int':int(age),'tec_age':{'str':str(tec_age),'int':int(tec_age)}},
                     'login':False}
        def figure(n_fname, n_lname, year):
            if (self.info['name']['first name'] == n_fname and self.info['name']['last name'] == n_lname) and ( self.today.year - year) == self.info['age']['tec_age']['int']:
                return True
            else:
                return False
        self.Noah = figure('Noah', 'Makowski', 2013)
        if self.Noah:
            self.info['Password'] = 'NOAH'
        self.Jonah = figure('Jonah', 'Makowski', 2010)
        if self.Jonah:
            self.info['Password'] = 'LOLA IS CUTE'
        self.admin_usr = False
        self.var = {'info':self.info,
                    'today':self.today,
                    'Noah':self.Noah,
                    'Jonah':self.Jonah,
                    'admin usr':self.admin_usr,
                    'pin':self.pin,
                    'shut off':self.shut_off}
        self.home()
    def login(self):
        while True:
            if self.Noah == False and self.Jonah == False:
                return 'Guest'
            else:
                password = input('What is the password ' + self.info['name']['first name'] + '?\n')
                if password == self.info['Password']:
                    if self.Jonah:
                        self.admin_login()
                    self.info['login'] = True
                    return True
                elif password != self.info['Password']:
                    self.kick_out()
    def admin_login(self):
        code_name = input('What is your codename ' + self.info['name']['first name'] + '  ')
        code_name_title = input('What is your codename title?  ')
        if code_name == 'Joe' and code_name_title == ", Lola's spy":
            pin = input("what is Jonah's pin?  ")
            if pin == str(self.pin):
                self.admin_usr = True
        else:
            self.kick_out()
    def kick_out(self):
        print('INCORRECT!')
        print('YOU ARE BEING KICKED OUT')
        print('LOADING')
        p = '-'
        from time import sleep
        length = 20
        dec = 0
        i = 0
        while True:
            print('')
            print(p + ' ({}%)'.format(str(dec)))
            sleep(1)
            dec = (i / length) * 100
            p = p + '-'
            i += 1
            if dec == 105:
                self.shut_off = True
                self.sleep()
    def sleep(self):
        if self.shut_off:
            print('Sleep has been activated')
            while True:
                pass
        else:
            print('you are being rederict back')
            return
    
    def home(self):
        d = self.login()
        if self.admin_usr:
            print('Welcome admin!')
            print('Now redirecting you to the admin page:')
            self.admin()
        if not self.shut_off:
            print('Welcome ' + self.info['name']['first name'] + '!')
            while True:
                pass
    def admin(self):
        if self.admin_usr == False or self.info['login'] == False:
            self.home()
        print('Welcome to admin {}!'.format(self.info['name']['first name']))
        print("Today's ({}) report".format(self.today.strftime("%d %B, %Y")))
        report = input("Today's report is that Lola is being very cute, and that she is the best dog ever\n")
        if report == 'y':
            self.pin = 1892
            pin = input("what is Jonah's pin?  ")
            if pin == str(self.pin):
                self.admin_usr = True
            if d == 'Guest' or self.admin_usr == False:
                self.home()
            else:
                print('opening real report:')

f_name = input('what is your (first) name?\n')
l_name = input('What is your last name?\nif you enter nothing, it will enter a guest\n')
if l_name == '':
    l_name = 'Guest'
while True:
    try:
        age = int(input('how old are you?\n'))
        break
    except:
        print('That is not a number')
while True:
    try:
        tec_age = int(input('what is your tec age?\nyour tec age is say you were born in 2009, and today it is the year 2021, then your tec age would be 12\n'))
        break
    except:
        print('That is not a number')
if tec_age == age:
    item = False
elif tec_age != age:
    item = True
if tec_age > age:
    _ = '+'
elif tec_age < age:
    _ = '-'
try:
    usr = Human(f_name, l_name, age, tec_age=item, _=_)
except:
    usr = Human(f_name, l_name, age, tec_age=item)
