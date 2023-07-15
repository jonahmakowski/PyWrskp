def create_board():
    row = []
    for c in range(COL_COUNT):
        row.append(0)
    board = []
    for r in range(ROW_COUNT):
        board.append(row.copy())
    return board


def show_board(board):
    print(chr(95) * (COL_COUNT * 2 + 3))
    for r in range(ROW_COUNT):
        print('[', *board[r], ']')
    print(chr(175) * (COL_COUNT * 2 + 3))
    print('[', *range(0, COL_COUNT), ']')


def get_player_input(player):
    col_valid = False
    while not col_valid:
        col_selected = input('Player ' + str(player) + ', Choose a column: ')
        col_valid = col_selected.isnumeric() and 0 <= int(col_selected) < COL_COUNT
    return int(col_selected)


def is_column_full(board, col):
    return board[0][col] != 0


def next_open_row(board, col):
    for row in range(ROW_COUNT - 1, -1, -1):  # 5,4,3,2,1,0
        if board[row][col] == 0:
            return row

def checks(b, p, c, r, c_change, r_change):
    found = 0
    counter_r = r_change
    counter_c = c_change
    while True:
        if COL_COUNT-1 >= c + counter_c >= 0 and ROW_COUNT-1 >= r + counter_r >= 0:
            if b[r + counter_r][c + counter_c] == p:
                found += 1
            else:
                break
        else:
            break
        if counter_r == 4*r_change and r_change != 0:
            break
        if counter_c == 4*c_change and c_change != 0:
            break
        counter_r += r_change
        counter_c += c_change
    return found

def is_a_winning_move(b, player, col, row):
    # horizontal
    horizontal = checks(b, player, col, row, 1, 0) + checks(b, player, col, row, -1, 0) + 1
    if horizontal >= 4:
        return True
    
    # vertical    
    vertical = checks(b, player, col, row, 0, 1) + checks(b, player, col, row, 0, -1) + 1
    if vertical >= 4:
        return True

    # diagonal UP
    diagonal_up = checks(b, player, col, row, 1, 1) + checks(b, player, col, row, -1, -1) + 1
    if diagonal_up >= 4:
        return True

    # diagonal DOWN
    diagonal_down = checks(b, player, col, row, -1, 1) + checks(b, player, col, row, 1, -1) + 1
    if diagonal_down >= 4:
        return True


# Beginning of the program
# Constants

COL_COUNT = 7
ROW_COUNT = 6

b = create_board()
show_board(b)

game_over = False
player = 1
while not game_over:

    col = get_player_input(player)

    if is_column_full(b, col):
        print('Sorry, that column is full')
    else:
        row = next_open_row(b, col)

        b[row][col] = player
        show_board(b)

        if is_a_winning_move(b, player, col, row):
            print('Player', player, 'WON')
            game_over = True

        player = player + 1
        if player == 3:
            player = 1
            