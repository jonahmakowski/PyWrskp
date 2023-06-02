m = int(input('What is the rate of change?'))
b = int(input('What is number zero?'))

mode = input('Would you like a list or one answer? (1/2)')

if mode == '1':
    x = 1
    threshold = 100000000000000000000000000000000000000000000
    while True:
        while x < threshold:
            print()
            print()
            number = m * x
            number += b
            print(number)
            print(x)
            x += 1
        cont = input('would you like to continue? y/n')
        if cont == 'n':
            break
        threshold += 100

elif mode == '2':
    x = int(input('What term are you looking for?'))
    number = m * x
    number += b
    print('That is {}!'.format(number))
