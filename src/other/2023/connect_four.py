import pyWrskp

board = {1: [' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
         2: [' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
         3: [' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
         4: [' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
         5: [' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
         6: [' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
         7: [' - ', ' - ', ' - ', ' - ', ' - ', ' - ']}


def print_board():
    print(' 1  2  3  4  5  6  7 ')
    for i in range(6):
        for c in range(1, 8):
            print(board[c][i], end='')
        print()


def get_col(player):
    while True:
        col = pyWrskp.number_input('Player {}, which colum would you like to go into?'.format(player))
        if not (col < 1 or col > 7):
            return col
        print('Number must be less then seven, and greater then one')


def all_checks(x, y, char, x_change, y_change):
    found = 0
    counter_x = x_change
    counter_y = y_change
    while True:
        if ((y + counter_y) <= 5 and (x + counter_x) <= 7) and ((y + counter_y) >= 0 and (x + counter_x) >= 1):
            if board[x+counter_x][y+counter_y] == char:
                found += 1
            else:
                break
        else:
            break
        if counter_x == 4*x_change and x_change != 0:
            break
        if counter_y == 4*y_change and y_change != 0:
            break
        counter_x += x_change
        counter_y += y_change
    return found


def check_win(current_move, char):
    if not current_move == [None, None]:
        x = current_move[0]
        y = current_move[1]

        horizontal = all_checks(x, y, char, 1, 0) + all_checks(x, y, char, -1, 0) + 1
        vertical = all_checks(x, y, char, 0, 1) + all_checks(x, y, char, 0, -1) + 1
        diagonal1 = all_checks(x, y, char, 1, 1) + all_checks(x, y, char, -1, -1) + 1
        diagonal2 = all_checks(x, y, char, -1, 1) + all_checks(x, y, char, 1, -1) + 1

        if horizontal >= 4:
            return True
        elif vertical >= 4:
            return True
        elif diagonal1 >= 4:
            return True
        elif diagonal2 >= 4:
            return True
        return False


def display_winner(win):
    print_board()
    print('Player {} has won the game of connect four!'.format(win))


winner = None
player1_col = None
player1_row = None
player2_col = None
player2_row = None


while True:
    print_board()
    player1_col = get_col('one')
    for i in range(5, -1, -1):
        if board[player1_col][i] == ' - ':
            board[player1_col][i] = ' X '
            player1_row = i
            break

    if check_win([player1_col, player1_row], ' X '):
        winner = 'one'
        break
    
    print()
    print()
    
    print_board()
    player2_col = get_col('two')
    for i in range(5, -1, -1):
        if board[player2_col][i] == ' - ':
            board[player2_col][i] = ' O '
            player2_row = i
            break

    print()
    print()

    if check_win([player2_col, player2_row], ' O '):
        winner = 'two'
        break
    
display_winner(winner)
