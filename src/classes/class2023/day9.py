# Functions
def create_board():
    b = []
    row = []
    for c in range(COL_COUNT):
        row.append(0)

    for r in range(ROW_COUNT):
        b.append(row.copy())

    return b


def show_board(b):
    print(chr(95)*(COL_COUNT*2+3))
    for r in range(ROW_COUNT):
        print('[', *b[r], ']')
    print(chr(175)*(COL_COUNT*2+3))
    print(' ', *range(COL_COUNT))


def get_player_input(p):
    while True:
        inp = input('Player {}, what col would you like?    '.format(p))
        if inp.isdigit():
            inp = int(inp)
            if 0 <= inp <= COL_COUNT - 1:
                break
            else:
                print('{} is not a vaild number'.format(inp))
        else:
            print('What ever "{}" '.format(inp) + "is, it isn't a number!")
    return inp


def get_full_col(c, b):
    return b[0][c] != 0


def drop(p, b, c):
    for i in range(ROW_COUNT-1, -1, -1):
        if board[i][c] == 0:
            board[i][c] = p
            r = i
            break
    return b, r


# Constants
COL_COUNT = 7
ROW_COUNT = 6

# Main Code
board = create_board()
show_board(board)

player = 1
game_over = False
while not game_over:
    while True:
        col = get_player_input(player)
        if get_full_col(col, board):
            print('This col is full, please choose a diffrent one.')
        else:
            break
    
    board, row = drop(player, board, col)
    show_board(board)
    
    if player == 1:
        player = 2
    else:
        player = 1
