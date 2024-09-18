from peices import Rook, Knight, Bishop, Queen, King, Pawn

class Board:
    def __init__(self):
        self.turn = 0
        self.board = []
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
                           Knight(1, 6, 1),
                           Bishop(2, 6, 1),
                           Queen(3, 6, 1),
                           King(4, 6, 1),
                           Bishop(5, 6, 1),
                           Knight(6, 6, 1),
                           Rook(7, 6, 1)])

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

    def move(self, location_start:tuple, location_end:tuple): # locations should be in (x, y) pairs
        self.board[location_start[0]][location_start[1]].position_x = location_end[0]
        self.board[location_start[0]][location_start[1]].position_y = location_end[1]
        copy_of_piece = self.board[location_start[0]][location_start[1]].copy()
        self.board[location_start[0]][location_start[1]] = 'X'
        self.board[location_end[0]][location_end[1]] = copy_of_piece

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

    def get_location(self, x, y):
        if x < 0 or y < 0:
            raise ValueError("x and y must be positive, not {} and {}".format(x, y))
        elif x > len(self.board) or y > len(self.board[0]):
            raise ValueError("x and y must be smaller than board")
        return self.board[y][x]
