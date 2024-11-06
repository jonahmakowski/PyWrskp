inp = input()

inp_lis = list(inp)

current = inp_lis[0]

bad = False

for item in inp_lis:
    if item != current:
        bad = True
    if current == 'Z':
        current = 'X'
    elif current == 'X':
        current = 'Z'

if bad:
    print('BAD')
else:
    print('GOOD')
    