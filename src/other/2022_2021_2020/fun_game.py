import time

name = input('What is your name?\n')

if name == ('Jonah'):
    password = input('What is the password?\n')

    if password != ('Jo'):
        exit()

if name != ('Jonah'):
    if name == ('Noah'):
        password = input('What is the password?\n')

        if password != ('No'):
            exit()
    
    if name != ('Noah'):
        exit()

print('Hello ' + name + ' welcome back!')

do = input('What would you like to do?\n')

if do == ('count'):
    count_how_long = int(input('What number should I count to ' + name + '?\n'))
    
    for i in range(count_how_long):
        time.sleep(1)
        print(str(i + 1))
    exit()

if do == ('turtle draw'):
    import turtle
    
    t = turtle.Turtle()
    
    t.speed(0)
    
    sides = int(input('How many sides would you like?\n'))
    
    length = int(input('How long would you like your sides to be?\n'))
    
    for i in range(sides):
        t.forward(length)
        t.right(360 / sides)
