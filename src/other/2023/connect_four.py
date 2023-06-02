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


while True:
    print_board()
    player1_col = pyWrskp.number_input('Player one, which colum would you like to go into?')
    