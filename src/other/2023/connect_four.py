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


def check_win(current_move1, current_move2):
    # Player one
    # Horizontal check
    x = current_move1[0]
    y = current_move2[1]
    if board[x+1][y] == 'X':
        pass
    


while True:
    print_board()
    player1_col = get_col('one')
    for i in range(5, -1, -1):
        if board[player1_col][i] == ' - ':
            board[player1_col][i] = ' X '
            player1_row = i
            break
    
    print()
    print()
    
    print_board()
    player2_col = get_col('two')
    for i in range(5, -1, -1):
        if board[player2_col][i] == ' - ':
            board[player2_col][i] = ' O '
            player1_row = i
            break
    if check_win([player1_col, player1_row], [player1_col, player1_row]):
        break
    