import PySimpleGUI as sg

def multiples(num, amount):
    multiples = []
    cur_multiple = num
    for i in range(amount):
        multiples.append(cur_multiple)
        cur_multiple += num
    return multiples

def factors(num):
    factors = []
    for x in range(1, num + 1):
        if num % x == 0:
            factors.append(x)
    return factors

def factor_pairs(num):
    factors = []
    nums = []
    for x in range(1, num + 1):
        if num % x == 0:
            if x not in nums:
                factors.append((x, int(num/x)))
                nums.extend([x, num/x])
    return factors

def display_multiples(num, amount):
    m = multiples(num, amount)
    sg.popup("The first {} multiples of {} are:\n{}".format(amount, num, m),
             line_width=200,
             title='Multiples')

def display_factors(num):
    f = factors(num)
    sg.popup("{} has {} factors.\nThe factors of {} are:\n{}".format(num, len(f), num, f),
             line_width=200,
             title='Factors')

def display_factors_pairs(num):
    f = factor_pairs(num)
    sg.popup("{} has {} factors pairs.\nThe factors pairs of {} are:\n{}".format(num, len(f), num, f),
             line_width=200,
             title='Factor Pairs')
