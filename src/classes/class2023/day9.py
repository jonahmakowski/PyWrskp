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


def get_player_input(p):
    print(' ', *range(COL_COUNT))
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
    return b[c][0] != 0


def drop(p, b, c):
    for i in range(ROW_COUNT-1, -1, -1):
        if board[i][c] == 0:
            board[i][c] = p
            r = i
            break
    return b, r


def win_check(x, y, p, x_change, y_change):
    found = 0
    counter_x = x_change
    counter_y = y_change
    while True:
        if ((y + counter_y) <= ROW_COUNT-1 and (x + counter_x) <= COL_COUNT-1) and ((y + counter_y) >= 0 and (x + counter_x) >= 0):
            if board[x+counter_x][y+counter_y] == p:
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


def all_win_checks(cur_move, p):
    x = cur_move[0]
    y = cur_move[1]

    horizontal = win_check(x, y, p, 1, 0) + win_check(x, y, p, -1, 0) + 1
    vertical = win_check(x, y, p, 0, 1) + win_check(x, y, p, 0, -1) + 1
    diagonal1 = win_check(x, y, p, 1, 1) + win_check(x, y, p, -1, -1) + 1
    diagonal2 = win_check(x, y, p, -1, 1) + win_check(x, y, p, 1, -1) + 1

    if horizontal >= 4:
        return True
    elif vertical >= 4:
        return True
    elif diagonal1 >= 4:
        return True
    elif diagonal2 >= 4:
        return True
    else:
        return False


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
    
    if all_win_checks([col, row], player):
        print('Player {} you won connect four!'.format(player))
        break
    
    if player == 1:
        player = 2
    else:
        player = 1
