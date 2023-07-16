import tkinter as tk
from time import sleep
from random import randint
import os


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.active = False
        self.pas = '4412342132'
        self.create_widgets()
        self.code = ''
    
    def create_widgets(self):
        self.btnFrame = tk.Frame(self)

        self.btns = [tk.Button(self.btnFrame, text='1', command=self.one),
                     tk.Button(self.btnFrame, text='2', command=self.two),
                     tk.Button(self.btnFrame, text='3', command=self.three),
                     tk.Button(self.btnFrame, text='4', command=self.four),
                     tk.Button(self.btnFrame, text='send', command=self.send),
                     tk.Button(self.btnFrame, text='del', command=self.d)]
        
        self.btnFrame.grid(row=0, column=0, sticky='ns')
        r, c = 0, 0
        for item in self.btns:
            item.grid(row=r, column=c, sticky='ew')
            r += 1

    def one(self):
        if not self.active:
            print('Enter the code')
            self.active = True
        else:
            print('1')
            self.code += '1'
    
    def two(self):
        if self.active:
            print('2')
            self.code += '2'
        else:
            print('Error Wrong Button')
    
    def three(self):
        if self.active:
            print('3')
            self.code += '3'
        else:
            print('Error Wrong Button')
        
    def four(self):
        if self.active:
            print('4')
            self.code += '4'
        else:
            print('Error Wrong Button')
    
    def d(self):
        if self.active:
            self.code = self.code[:len(self.code)-1]
            print(self.code)
            print('del')
        else:
            print('Error Wrong Button')
    
    def send(self):
        if self.code == self.pas:
            self.master.destroy()
        else:
            print('FAIL, SYSTEM SHUTTING DOWN')
            exit()


root = tk.Tk()
root.title('Login')

root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=600, weight=1)

app = Application(master=root)
app.mainloop()


class System(tk.Frame):
    def __init__(self, usr, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.usr = usr
        self.create_buttons_btns()
        self.runtime = 0

    def create_buttons_btns(self):
        self.btnFrame = tk.Frame(self)

        self.btns = [
            {'loc': [10, 10], 'item': tk.Button(self.btnFrame, text='log out', command=self.master.destroy)},
            {'loc': [0, 0], 'item': tk.Button(self.btnFrame, text='Info', command=self.info)}]
        self.create_buttons()

    def create_buttons(self):
        self.btnFrame.grid(row=0, column=0, sticky='ns')
        for item in self.btns:
            r = item['loc'][0]
            c = item['loc'][1]
            item['item'].grid(row=r, column=c, sticky='ew')

    def info(self):
        print('\n\n\n\n\n\n\n')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('~~~~~~~~~~~~~~~~~~         ~~~~~~~~~~~~~~~~~~')
        print('~~~~~~~~~~~~~~~~~~  Hello  ~~~~~~~~~~~~~~~~~~')
        print('~~~~~~~~~~~~~~~~~~         ~~~~~~~~~~~~~~~~~~')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        sleep(5)
        print('\n\n\n\n\n\n\n')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('~~~~~~~~~~~~~~~~~~~~~~                                                ~~~~~~~~~~~~~~~~~~~~~~')
        print('~~~~~~~~~~~~~~~~~~~~~~ This system is owned and run by Jonah Makowski ~~~~~~~~~~~~~~~~~~~~~~')
        print('~~~~~~~~~~~~~~~~~~~~~~                                                ~~~~~~~~~~~~~~~~~~~~~~')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        sleep(4)
        print('\n\n\n\n\n\n\n')
        print('as you know the passcode is {}'.format(app.pas))


if app.active and app.pas == app.code:
    os.system('clear')
    print('system active')
    print('setting up system')
    sleep(randint(1, 10))
    
    print('~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~   Hi   ~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~')
    
    sleep(5)
    print('\n\n\n')
    
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~  WELCOME TO SYSTEM  ~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
    sleep(5)
    print('\n\n\n')
    
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~   What is your name   ~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    name = input()
    
    if (name == 'Jonah' or name == 'Noah') or (name == 'Jonah Makowski' or name == 'Noah Makowski'):
        sleep(2.5)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('~~~~~~~~  SYSTEM 100% ACTIVE  ~~~~~~~~')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # system
        print('Hi {} welcome to the system!'.format(name))
        root2 = tk.Tk()
        root2.title('System')

        root2.rowconfigure(0, minsize=800, weight=1)
        root2.columnconfigure(1, minsize=600, weight=1)

        system = System(name, master=root2)
        system.mainloop()
    else:
        exit()
