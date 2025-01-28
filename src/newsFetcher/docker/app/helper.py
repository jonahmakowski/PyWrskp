def printf(*args, sep=' '):
    try:
        with open('python.log', 'r') as f:
            data = f.read()
    except FileNotFoundError:
        data = ''
    
    for arg in args:
        data += str(arg) + str(sep)

    print(data)

    data += '\n'
    
    with open('python.log', 'w') as f:
        f.write(data)

def log_clear():
    with open('python.log', 'w') as f:
        f.write('')
