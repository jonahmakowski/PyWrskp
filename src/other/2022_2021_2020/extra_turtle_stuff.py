def draw_hex(sides, length_of_sides, t):
    for i in range(sides):
        t.forward(length_of_sides)
        t.right(360 / sides)

def turn(length, turn, left_or_right, t):
    if left_or_right == 'right':
        for i in range(length):
            t.forward(1)
            t.right(turn)
    elif left_or_right == 'left':
        for i in range(length):
            t.forward(1)
            t.left(turn)
    else:
        print('you have an error with the fuction "turn", becasue for left_or_right, you put in {}, not left or right'.format(left_or_right))