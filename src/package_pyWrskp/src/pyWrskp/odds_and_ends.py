def number_input(question,
                 t='int',
                 new_line=False,
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
