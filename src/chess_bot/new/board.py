from peices import Rook, Knight, Bishop, Queen, King, Pawn, ChessPiece


class Board:
    def __init__(self, board=None):
        self.board = [] if board is None else board
        if board is None:
            self.generate_board()

    def generate_board(self):
        self.board = []
        self.board.append([Rook(0, 0, 0),
                           Knight(1, 0, 0),
                           Bishop(2, 0, 0),
                           Queen(3, 0, 0),
                           King(4, 0, 0),
                           Bishop(5, 0, 0),
                           Knight(6, 0, 0),
                           Rook(7, 0, 0)])
        self.board.append([Pawn(0, 1, 0),
                           Pawn(1, 1, 0),
                           Pawn(2, 1, 0),
                           Pawn(3, 1, 0),
                           Pawn(4, 1, 0),
                           Pawn(5, 1, 0),
                           Pawn(6, 1, 0),
                           Pawn(7, 1, 0)])
        for _ in range(4):
            self.board.append([None, None, None, None, None, None, None, None])

        self.board.append([Pawn(0, 6, 1),
                           Pawn(1, 6, 1),
                           Pawn(2, 6, 1),
                           Pawn(3, 6, 1),
                           Pawn(4, 6, 1),
                           Pawn(5, 6, 1),
                           Pawn(6, 6, 1),
                           Pawn(7, 6, 1)])
        self.board.append([Rook(0, 6, 1),
                           Knight(1, 7, 1),
                           Bishop(2, 7, 1),
                           Queen(3, 7, 1),
                           King(4, 7, 1),
                           Bishop(5, 7, 1),
                           Knight(6, 7, 1),
                           Rook(7, 7, 1)])

    def pr(self):
        if self.board is None:
            raise ValueError("Board is None")

        cur_row = 0
        for row in self.board:
            for piece in row:
                if piece is not None:
                    print(str(piece), end='\t')
                else:
                    print('X', end='\t')
            print(cur_row)
            cur_row += 1
        print('0\t1\t2\t3\t4\t5\t6\t7')
        print()
        white_points, black_points = self.calculate_points()
        print('White has {} points, Black has {} points.'.format(white_points-10000, black_points-10000))
        print()

    def move(self, location_start:tuple, location_end:tuple): # locations should be in (x, y) pairs
        print('Board.py Line 68', self.board)
        print('Board.py Line 69', self.board[location_start[1]][location_start[0]])
        self.board[location_start[1]][location_start[0]].position_x = location_end[0]
        self.board[location_start[1]][location_start[0]].position_y = location_end[1]
        copy_of_piece = self.board[location_start[1]][location_start[0]].copy()
        self.board[location_start[1]][location_start[0]] = None
        self.board[location_end[1]][location_end[0]] = copy_of_piece

    def calculate_points(self):
        white_points = 0
        black_points = 0
        for row in self.board:
            for piece in row:
                if piece is not None:
                    if piece.side == 0:
                        white_points += piece.value
                    elif piece.side == 1:
                        black_points += piece.value

        return white_points, black_points

    def get_pieces(self):
        white_pieces = []
        black_pieces = []
        for row in self.board:
            for piece in row:
                if piece is not None:
                    if piece.side == 0:
                        white_pieces.append(piece)
                    elif piece.side == 1:
                        black_pieces.append(piece)

        return white_pieces, black_pieces

    def win_check(self):
        white_win = True
        black_win = True
        white, black = self.get_pieces()
        for piece in white:
            if type(piece) is King:
                black_win = False
        for piece in black:
            if type(piece) is King:
                white_win = False

        return white_win, black_win

    def get_location(self, x, y):
        if x < 0 or y < 0:
            raise ValueError("x and y must be positive, not {} and {}".format(x, y))
        elif x > len(self.board) or y > len(self.board[0]):
            raise ValueError("x and y must be smaller than board")
        return self.board[y][x]

    def copy(self):
        new_board = [row.copy() for row in self.board]
        return self.__class__(new_board)

    def promote(self, piece:ChessPiece):
        self.board[piece.position_y][piece.position_x] = Queen(piece.position_x, piece.position_y, piece.side)
