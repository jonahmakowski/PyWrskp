from time import sleep


def number_input(question,
                 t='int',
                 new_line=True,
                 tell=True):
    if tell:
        question += ' (This must be a number)'
    if new_line:
        question += '\n'
    while True:
        try:
            if t == 'int':
                a = int(input(question))
            else:
                a = float(input(question))
            break
        except ValueError:
            print('That is not a number!\n' +
                  'Try again')
    return a


def loading(time):
    loops = int(time * 1.5)
    for i in range(loops):
        print('|', end="\r")
        sleep(0.5)
        print('/', end="\r")
        sleep(0.5)
        print('-', end="\r")
        sleep(0.5)
