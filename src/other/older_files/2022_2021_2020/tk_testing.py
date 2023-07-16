import tkinter as tk

labels = {}
buttons = {}
entrys = {}

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 1000, height = 1000/2,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Calculate')
label1.config(font=('helvetica', 14))
canvas1.create_window(1000/2, 25, window=label1)
labels['label1'] = label1

entry1 = tk.Entry(root, justify='center')
entry1.place(x=0, y=100, width=1000, height=25)
#canvas1.create_window(1000/2, 100, window=entry1)

entry2 = tk.Entry(root, justify='center')
entry2.place(x=0, y=150, width=1000, height=25)
#canvas1.create_window(1000/2, 150, window=entry2)

e3 = 0
label4 = 0
def fuction(e3):
    global label4
    label4 = tk.Label(root, text=e3, font=('helvetica', 9))
    canvas1.create_window(1000/2, 140, window=label4)
    labels['label4'] = label4
def m():
    global e3
    e3 = '*'
    fuction(e3)
def d():
    global e3
    e3 = '/'
    fuction(e3)
def a():
    global e3
    e3 = '+'
    fuction(e3)
def s():
    global e3
    e3 = '-'
    fuction(e3)

def cac():
    global a
    global e1
    global e2
    global e3
    if e1 == '' or e2 == '':
        return
    e1 = int(entry1.get())
    e2 = int(entry2.get())
    
    if e3 == '+':
        a = e1 + e2
    elif e3 == '-':
        a = e1 - e2
    elif e3 == '*':
        a = e1 * e2
    elif e3 == '/':
        a = e1 / e2
    text = '{} {} {} = {}'.format(e1, e3, e2, a)
    if len(text) > 150:
        text = '{}'.format(e1)
        
        text2 = '{}'.format(e3)
        
        text3 = '{}'.format(e2)
        
        text4 = '='
        
        text5 = '{}'.format(a)
        
        height = 270
        adding = 25
        global label5
        global label6
        global label7
        global label8
        global label4
        label4 = tk.Label(root, text=text,font=('helvetica', 10))
        canvas1.create_window(1000/2, height, window=label4)
        labels['label4'] = label4
        
        height += adding
        
        label5 = tk.Label(root, text=text2,font=('helvetica', 10))
        canvas1.create_window(1000/2, height, window=label5)
        labels['label4'] = label4
        
        height += adding
        
        label6 = tk.Label(root, text=text3,font=('helvetica', 10))
        canvas1.create_window(1000/2, height, window=label6)
        labels['label6'] = label6
        
        height += adding
        
        label7 = tk.Label(root, text=text4,font=('helvetica', 10))
        canvas1.create_window(1000/2, height, window=label7)
        labels['label7'] = label7
        
        height += adding
        
        label8 = tk.Label(root, text=text5,font=('helvetica', 10))
        canvas1.create_window(1000/2, height, window=label8)
        labels['label8'] = label8
    else:
        global label3
        label3 = tk.Label(root, text=text,font=('helvetica', 10))
        canvas1.create_window(1000/2, 270, window=label3)
        labels['label3'] = label3
    print('{} {} {} = {}'.format(e1, e3, e2, a))
def clear():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    label4.destroy()
    try:
        label3.destroy()
        del labels['label3']
    except:
        label4.destroy()
        del labels['label4']
        label5.destroy()
        del labels['label5']
        label6.destroy()
        del labels['label6']
        label7.destory()
        del labels['label7']
        label8.destory()
        del labels['label8']

num = 430
height = 225
add = 37

button6 = tk.Button(text='C', command=clear, font=('helvetica', 11, 'bold'))
canvas1.create_window(1000/2, 450, window=button6)

button2 = tk.Button(text='*', command=m, font=('helvetica', 9, 'bold'))
canvas1.create_window(num, height, window=button2)

num += add
button3 = tk.Button(text='/', command=d, font=('helvetica', 9, 'bold'))
canvas1.create_window(num, height, window=button3)

num += add
button4 = tk.Button(text='+', command=a, font=('helvetica', 9, 'bold'))
canvas1.create_window(num, height, window=button4)

num += add
button5 = tk.Button(text='-', command=s, font=('helvetica', 9, 'bold'))
canvas1.create_window(num, height, window=button5)

num += add
button1 = tk.Button(text='=', command=cac, font=('helvetica', 9, 'bold'))
canvas1.create_window(num, height, window=button1)

a = 0
e1 = 0
e2 = 0

root.mainloop()
