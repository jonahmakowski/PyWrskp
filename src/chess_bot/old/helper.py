from random import randint
import threading
from time import sleep


class ChessBoard:
    def __init__(self, board=None, turn='White', turn_count=0):
        """
        In the board the following numbers equal various chess pieces
        Anything with an A = white
        Anything with an B = black

        Numbers for pieces:
        1 = pawn
        2 = rook
        3 = knight
        4 = bishop
        5 = queen
        6 = king

        So for example, 6A is the white king
        00 means that there is nothing there/empty square
        """

        self.board = self.start_board() if board is None else board
        self.winner = None
        self.white_score = 0
        self.black_score = 0
        self.turn = turn
        self.turn_count = turn_count
        self.black_castle = True
        self.white_castle = True
        self.point_values = {'Pawn': 1, 'Knight': 3, 'Bishop': 3, 'Rook': 5, 'Queen': 9, 'King': 15}
        self.bot_access = Bot(0)

    def check(self, color):
        opponent_moves = self.bot_access.find_options_helper(self.clone(),
                                                             'A' if color == 'B' else 'B',
                                                             '',
                                                             check=False)

        for move in opponent_moves:
            for part in move:
                pieces = part['newBoard'].player_pieces(color)
                for piece in pieces:
                    if piece[2] == '6':
                        return True
        return False

    @staticmethod
    def start_board():
        board = [['2A', '3A', '4A', '5A', '6A', '4A', '3A', '2A'],
                 ['1A', '1A', '1A', '1A', '1A', '1A', '1A', '1A'],
                 ['00', '00', '00', '00', '00', '00', '00', '00'],
                 ['00', '00', '00', '00', '00', '00', '00', '00'],
                 ['00', '00', '00', '00', '00', '00', '00', '00'],
                 ['00', '00', '00', '00', '00', '00', '00', '00'],
                 ['1B', '1B', '1B', '1B', '1B', '1B', '1B', '1B'],
                 ['2B', '3B', '4B', '5B', '6B', '4B', '3B', '2B']]
        return board.copy()

    def display_board(self):
        print('\t0\t1\t2\t3\t4\t5\t6\t7')
        y_counter = 0
        for row in self.board:
            print(y_counter, end='\t')
            for location in row:
                match location:
                    case '1A':
                        print('♙', end='\t')
                    case '2A':
                        print('♖', end='\t')
                    case '3A':
                        print('♘', end='\t')
                    case '4A':
                        print('♗', end='\t')
                    case '5A':
                        print('♕', end='\t')
                    case '6A':
                        print('♔', end='\t')
                    case '1B':
                        print('♟', end='\t')
                    case '2B':
                        print('♜', end='\t')
                    case '3B':
                        print('♞', end='\t')
                    case '4B':
                        print('♝', end='\t')
                    case '5B':
                        print('♛', end='\t')
                    case '6B':
                        print('♚', end='\t')
                    case '00':
                        print('⬛', end='\t')
            y_counter += 1
            print('')
        print('Current Score: White: {}, Black: {}'.format(self.white_score,
                                                           self.black_score))
        print('Current Turn: {}; Turn #{}'.format(self.turn, self.turn_count))

    def get_location(self, x, y):
        return self.board[y][x]

    def player_pieces(self, color):
        pieces = []
        y = 0
        for row in self.board:
            x = 0
            for location in row:
                if color in location:
                    pieces.append((x, y, location[0]))
                x += 1
            y += 1
        return pieces

    def move(self, x1, y1, x2, y2):
        self.board[y2][x2] = self.board[y1][x1]
        self.board[y1][x1] = '00'
        self.turn = 'White' if self.turn == 'Black' else 'White'
        self.turn_count += 1
        self.calculate_score()

    def calculate_score(self):
        zero_points = (self.point_values['Pawn'] * 8
                       + self.point_values['Knight'] * 2
                       + self.point_values['Bishop'] * 2
                       + self.point_values['Rook'] * 2
                       + self.point_values['Queen']
                       + self.point_values['King'])
        white_on_table = 0
        black_on_table = 0

        white_pieces = self.player_pieces('A')
        black_pieces = self.player_pieces('B')

        for piece in white_pieces:
            match piece[2]:
                case '1':
                    white_on_table += self.point_values['Pawn']
                case '2':
                    white_on_table += self.point_values['Rook']
                case '3':
                    white_on_table += self.point_values['Knight']
                case '4':
                    white_on_table += self.point_values['Bishop']
                case '5':
                    white_on_table += self.point_values['Queen']
                case '6':
                    white_on_table += self.point_values['King']

        for piece in black_pieces:
            match piece[2]:
                case '1':
                    black_on_table += self.point_values['Pawn']
                case '2':
                    black_on_table += self.point_values['Rook']
                case '3':
                    black_on_table += self.point_values['Knight']
                case '4':
                    black_on_table += self.point_values['Bishop']
                case '5':
                    black_on_table += self.point_values['Queen']
                case '6':
                    black_on_table += self.point_values['King']
        self.white_score = zero_points - black_on_table
        self.black_score = zero_points - white_on_table

    def clone(self):
        copy = []
        for row in self.board:
            copy.append(row.copy())
        return ChessBoard(board=copy, turn=self.turn, turn_count=self.turn_count)


class Bot:
    def __init__(self, moves_ahead):
        # Bot is always black
        self.moves_ahead = moves_ahead
        self.options = []

    def calculate_moves(self, board: ChessBoard):
        self.options = []
        self.find_options_first(board, self.moves_ahead, 'B')

        while threading.active_count() != 1:
            sleep(1)

        best_score_difference = -100
        for option in self.options:
            if option['blackPoints'] - option['whitePoints'] > best_score_difference:
                best_score_difference = option['blackPoints'] - option['whitePoints']

        best_options = []
        for option in self.options:
            if option['blackPoints'] - option['whitePoints'] == best_score_difference:
                best_options.append(option)

        if len(best_options) == 1:
            index = 0
        else:
            index = randint(0, len(best_options) - 1)

        self.options = []

        return best_options[index]['firstMove']['newBoard'].clone()

    def find_options_first(self, board: ChessBoard, moves, side):
        cur_options = self.find_options_helper(board.clone(), side, '')
        if moves <= 0:
            if side == 'A':
                for option in cur_options:
                    self.new_search_thread(option['newBoard'], moves - 1, 'B' if side == 'A' else 'A', option)
                    return
            for option in cur_options:
                self.options.append(option)
                return
        else:
            for option in cur_options:
                self.new_search_thread(option['newBoard'], moves - 1, 'B' if side == 'A' else 'A', option)
                return

    def find_options_main(self, board: ChessBoard, moves, side, first_option):
        cur_options = self.find_options_helper(board.clone(), side, first_option)
        if moves <= 0:
            if side == 'A':
                for option in cur_options:
                    self.new_search_thread(option['newBoard'], moves - 1, 'B' if side == 'A' else 'A', first_option)
                return
            else:
                for option in cur_options:
                    self.options.append(option)
                return
        else:
            for option in cur_options:
                self.new_search_thread(option['newBoard'], moves - 1, 'B' if side == 'A' else 'A', first_option)
            return

    def new_search_thread(self, board, moves, side, first_option):
        x = threading.Thread(target=self.find_options_main, args=(board, moves, side, first_option,))
        x.start()

    def find_options_helper(self, board: ChessBoard, side, first_move, options=None, check=True):
        if options is None:
            options = []
        pieces = board.player_pieces(side)
        for piece in pieces:
            x, y, t = piece
            match t:
                case '1':
                    possible = range(0, 7)
                    if side == 'B':
                        if y == 6 and board.get_location(x, y - 2) == '00':
                            options = self.append_options((x, y), (x, y - 2), board, options, side, first_move, check)
                        if y - 1 in possible and board.get_location(x, y - 1) == '00':
                            options = self.append_options((x, y), (x, y - 1), board, options, side, first_move, check)
                        if (y - 1 in possible and x + 1 in possible) and board.get_location(x + 1, y - 1) != '00':
                            options = self.append_options((x, y), (x + 1, y - 1), board, options, side, first_move,
                                                          check)
                        if (y - 1 in possible and x - 1 in possible) and board.get_location(x - 1, y - 1) != '00':
                            options = self.append_options((x, y), (x - 1, y - 1), board, options, side, first_move,
                                                          check)
                    elif side == 'A':
                        if y == 1 and board.get_location(x, y + 2) == '00':
                            options = self.append_options((x, y), (x, y + 2), board, options, side, first_move, check)
                        if y + 1 in possible and board.get_location(x, y + 1) == '00':
                            options = self.append_options((x, y), (x, y + 1), board, options, side, first_move, check)
                        if (y + 1 in possible and x + 1 in possible) and board.get_location(x + 1, y + 1) != '00':
                            options = self.append_options((x, y), (x + 1, y + 1), board, options, side, first_move,
                                                          check)
                        if (y + 1 in possible and x - 1 in possible) and board.get_location(x - 1, y + 1) != '00':
                            options = self.append_options((x, y), (x - 1, y + 1), board, options, side, first_move,
                                                          check)
                case '2':
                    options = self.check_straights((x, y), board, options, side, first_move, check)
                case '3':
                    options = self.append_options((x, y), (x - 1, y + 2), board, options, side, first_move, check)
                    options = self.append_options((x, y), (x + 1, y + 2), board, options, side, first_move, check)
                    options = self.append_options((x, y), (x - 1, y - 2), board, options, side, first_move, check)
                    options = self.append_options((x, y), (x + 1, y - 2), board, options, side, first_move, check)

                    options = self.append_options((x, y), (x - 2, y + 1), board, options, side, first_move, check)
                    options = self.append_options((x, y), (x + 2, y + 1), board, options, side, first_move, check)
                    options = self.append_options((x, y), (x - 2, y - 1), board, options, side, first_move, check)
                    options = self.append_options((x, y), (x + 2, y - 1), board, options, side, first_move, check)
                case '4':
                    options = self.check_diagonals((x, y), board, options, side, first_move, check)
                case '5':
                    options = self.check_diagonals((x, y), board, options, side, first_move, check)
                    options = self.check_straights((x, y), board, options, side, first_move, check)
                case '6':
                    options = self.append_options((x, y), (x + 1, y), board, options, side, first_move, check)
                    options = self.append_options((x, y), (x + 1, y + 1), board, options, side, first_move, check)
                    options = self.append_options((x, y), (x, y + 1), board, options, side, first_move, check)
                    options = self.append_options((x, y), (x, y - 1), board, options, side, first_move, check)
                    options = self.append_options((x, y), (x - 1, y - 1), board, options, side, first_move, check)
                    options = self.append_options((x, y), (x - 1, y), board, options, side, first_move, check)
                    options = self.append_options((x, y), (x + 1, y - 1), board, options, side, first_move, check)
                    options = self.append_options((x, y), (x - 1, y + 1), board, options, side, first_move, check)
        return options

    @staticmethod
    def append_options(xy, xy2, board: ChessBoard, options: list, side: str, first_move, check):
        if (xy2[0] < 0 or xy2[0] > 7) or (xy2[1] < 0 or xy2[1] > 7):
            return options

        at_xy2 = board.get_location(xy2[0], xy2[1])
        if side in at_xy2:
            return options

        option = board.clone()
        option.move(xy[0], xy[1], xy2[0], xy2[1])
        if check:
            if not option.check(side):
                options.append({'newBoard': option,
                                'whitePoints': option.white_score,
                                'blackPoints': option.black_score,
                                'firstMove': first_move})

        return options

    def check_diagonals(self, xy, board, options, side, first_move, check):
        x, y = xy
        options = self.direction_check((x, y), (1, 1), board, options, side, first_move, check)
        options = self.direction_check((x, y), (-1, 1), board, options, side, first_move, check)
        options = self.direction_check((x, y), (1, -1), board, options, side, first_move, check)
        options = self.direction_check((x, y), (-1, -1), board, options, side, first_move, check)
        return options

    def check_straights(self, xy, board, options, side, first_move, check):
        x, y = xy
        options = self.direction_check((x, y), (1, 0), board, options, side, first_move, check)
        options = self.direction_check((x, y), (-1, 0), board, options, side, first_move, check)
        options = self.direction_check((x, y), (0, 1), board, options, side, first_move, check)
        options = self.direction_check((x, y), (0, -1), board, options, side, first_move, check)
        return options

    def direction_check(self, xy, direction, board, options, side, first_move, check):
        x, y = xy
        x_dir, y_dir = direction
        x_counter = 0
        y_counter = 0
        while True:
            if x + x_counter > 7 or y + y_counter < 0:
                break
            elif y + y_counter > 7 or y + y_counter < 0:
                break
            elif (board.get_location(x + x_counter, y + y_counter) == '00'
                  or side not in board.get_location(x + x_counter, y + y_counter)):
                self.append_options((x, y), (x + x_counter, y + y_counter), board, options, side, first_move, check)
            else:
                break
            x_counter += x_dir
            y_counter += y_dir

        return options
