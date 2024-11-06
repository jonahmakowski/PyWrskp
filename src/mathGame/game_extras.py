from random import randint

def add(min_num, max_num):
    num1 = randint(max_num, min_num)
    num2 = randint(max_num, min_num)
    a = num1 + num2
    return num1, num2, a

def sub(min_num, max_num, neg):
    num1 = randint(max_num, min_num)
    num2 = randint(max_num, min_num)
    a = num1 - num2
    if neg == 'n' and a < 0:
        numq = num1
        numw = num2
        
        num1 = numw
        num2 = numq
        
        a = num1 - num2
        if neg == 'n' and a < 0:
            a = sub(max_num, min_num, neg)
    return num1, num2, a

def multi(min_num, max_num):
    num1 = randint(max_num, min_num)
    num2 = randint(max_num, min_num)
    a = num1 * num2
    return num1, num2, a

def div(min_num, max_num, dec):
    num1 = randint(max_num, min_num)
    num2 = randint(max_num, min_num)
    a = num1 / num2
    if dec == 'n' and isinstance(a, float):
        num1, num2, a = div(max_num, min_num, dec)
    return num1, num2, a