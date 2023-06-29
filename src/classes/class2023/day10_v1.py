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


def is_a_winning_move(b, player):
    # horizontal
    for r in range(0, ROW_COUNT):  # 0-5
        for c in range(0, COL_COUNT - 3):  # 0-3
            if b[r][c] == b[r][c + 1] == b[r][c + 2] == b[r][c + 3] == player:
                return True
    # vertical    
    for c in range(0, COL_COUNT):  # 0 - COL_COUNT
        for r in range(0, ROW_COUNT - 3):  # 0-ROW_COUNT-3
            if b[r][c] == b[r + 1][c] == b[r + 2][c] == b[r + 3][c] == player:
                return True

    # diagonal UP
    for c in range(0, COL_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if b[r][c] == b[r - 1][c + 1] == b[r - 2][c + 2] == b[r - 3][c + 3] == player:
                return True

    # diagonal DOWN
    for c in range(0, COL_COUNT-3):
        for r in range(0, ROW_COUNT-3):
            if b[r][c] == b[r + 1][c + 1] == b[r + 2][c + 2] == b[r + 3][c + 3] == player:
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

        if is_a_winning_move(b, player):
            print('Player', player, 'WON')
            game_over = True

        player = player + 1
        if player == 3:
            player = 1
