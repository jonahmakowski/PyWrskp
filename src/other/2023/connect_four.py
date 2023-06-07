import pyWrskp

board = {1: [' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
         2: [' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
         3: [' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
         4: [' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
         5: [' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
         6: [' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
         7: [' - ', ' - ', ' - ', ' - ', ' - ', ' - ']}


def print_board():
    for i in range(6):
        for c in range(1, 8):
            print(board[c][i], end='')
        print()


def get_col(player):
    while True:
        col = pyWrskp.number_input('Player {}, which colum would you like to go into?'.format(player))
        if not col < 1 or col > 7:
            return col
        print('Number must be less then seven, and greater then one')


def horizontal_check(x, y):
    horizontal_found = 0
    counter = 1
    while True:
        if not (x + counter) > 7:
            if board[x+counter][y] == 'X':
                horizontal_found += 1
        else:
            break
        if counter == 3:
            break
        counter += 1

    counter = 1

    while True:
        if not (x - counter) < 1:
            if board[x-counter][y] == 'X':
                horizontal_found += 1
        else:
            break
        if counter == 3:
            break
        counter += 1

    return horizontal_found


def check_win(current_move):
    if not current_move == [None, None]:
        # Player one
        # Horizontal check
        x = current_move[0]
        y = current_move[1]
        if horizontal_check(x, y) >= 4:
            return True
        return False


def display_winner(win):
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

    if check_win([player1_col, player1_row]):
        winner = 1
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

    if check_win([player2_col, player2_row]):
        winner = 2
        break
    
display_winner(winner)
