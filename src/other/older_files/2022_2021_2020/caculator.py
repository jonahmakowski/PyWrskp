# This is a simple calculator in the shell

def use(num1, t, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if t == '+':
            a = num1 + num2
            q = '{} + {}'.format(num1, num2)
        elif t == '-':
            a = num1 - num2
            q = '{} - {}'.format(num1, num2)
        elif t == '*':
            a = num1 * num2
            q = '{} * {}'.format(num1, num2)
        elif t == '/':
            a = num1 / num2
            q = '{} / {}'.format(num1, num2)
        elif t == '**':
            a = num1 ** num2
            q = '{} ** {}'.format(num1, num2)
        elif t == '^':
            from math import sqrt
            a = sqrt(num1)
            q = '√{}'.format(num1)
        else:
            a = "ISSUE CODE CAN NOT FIND NUMBERS NECESSARY, TALK TO THE OWNER OF THIS WEBSITE"
            q = a
    except AssertionError as error:
        q = error
        a = 'The linux_interaction() function was not executed'
    except ValueError as error:
        q = error
        a = 'The first or other string is not a int or float'
    return q, a


c, d = use(input('What is the first number?'), input('What is the type?'), input('what is the other number?'))
print(str(c) + ' = ' + str(d))
