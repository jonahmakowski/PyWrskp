class ChessPiece:
    def __init__(self, position_x, position_y, moves, name, side, appearance, value):
        self.position_x = position_x
        self.position_y = position_y
        self.name = name
        self.side = side # 0 is white, 1 is back
        self.moves = moves # Moves are formatted as tuples in a list, tuples should have x, y movement values for each
        self.appearance = appearance
        self.value = value

    def __str__(self):
        return self.appearance

    def debug(self):
        return "White {} at {}, {}".format(self.name, self.position_x,
                                           self.position_y) if self.side == 0 else "Black {} at {}, {}".format(
            self.name, self.position_x, self.position_y)

    def get_pos(self):
        return self.position_x, self.position_y

    def copy(self):
        return self.__class__(self.position_x, self.position_y, self.side)

    def list_moves(self, board):
        legal_moves = []
        for move in self.moves:
            if not ((self.position_x + move[0] < 0 or self.position_y + move[1] < 0) or
                    (self.position_x + move[0] > 7 or self.position_y + move[1] > 7)):
                if board.get_location(self.position_x + move[0], self.position_y + move[1]) is None:
                    legal_moves.append((self.position_x + move[0], self.position_y + move[1]))
                    #print('Found empy square')
                elif board.get_location(self.position_x + move[0], self.position_y + move[1]).side != self.side:
                    #print('Found occupied square by enemy')
                    legal_moves.append((self.position_x + move[0], self.position_y + move[1]))
        return legal_moves

    def check_range(self, start:int, end:int, x_change:int, y_change:int, b):
        moves = []
        direction = -1 if end < start else 1
        cur_x = x_change
        cur_y = y_change

        #print('Piece is at {}, {}'.format(self.position_x, self.position_y))

        for distance in range(start, end, direction):
            if self.position_x + cur_x > 7 or self.position_y + cur_y > 7:
                # print('Something is greater than 7 at {}, {}'.format(self.position_x + cur_x, self.position_y + cur_y))
                break
            elif self.position_x + cur_x < 0 or self.position_y + cur_y < 0:
                # print('Something is less than 0 at {}, {}'.format(self.position_x + cur_x, self.position_y + cur_y))
                break
            elif b.get_location(self.position_x + cur_x, self.position_y + cur_y) is None:
                # print('Found open square at {}, {}'.format(self.position_x + cur_x, self.position_y + cur_y))
                moves.append((self.position_x + cur_x, self.position_y + cur_y))
            elif b.get_location(self.position_x + cur_x, self.position_y + cur_y) is not None:
                if b.get_location(self.position_x + cur_x, self.position_y + cur_y).side != self.side:
                    # print('Found enemy at {}, {}'.format(self.position_x + cur_x, self.position_y + cur_y))
                    moves.append((self.position_x + cur_x, self.position_y + cur_y))
                    break
                else:
                    # print('Found friendly at {}, {}'.format(self.position_x + cur_x, self.position_y + cur_y))
                    break

            cur_x += x_change
            cur_y += y_change

        return moves

class Pawn(ChessPiece):
    def __init__(self, position_x, position_y, side):
        moves = [(0, 1)]
        appearance = '♟' if side == 1 else '♙'
        super().__init__(position_x, position_y, moves, "Pawn", side, appearance, 1)
    def list_moves(self, board):
        legal_moves = []

        b = board.board

        # Moving two forward from a starting position
        if ((self.side == 0 and b[self.position_y+2][self.position_x] is None)
                and b[self.position_y+1][self.position_x] is None):
            legal_moves.append((self.position_x, self.position_y + 2))
        elif ((self.side == 1 and b[self.position_y-2][self.position_x] is None)
              and b[self.position_y-1][self.position_x] is None):
            legal_moves.append((self.position_x, self.position_y - 2))

        # Moving one forward
        if self.side == 0 and b[self.position_y+1][self.position_x] is None:
            legal_moves.append((self.position_x, self.position_y+1))
        elif self.side == 1 and b[self.position_y-1][self.position_x] is None:
            legal_moves.append((self.position_x, self.position_y-1))

        #Taking
        if 0 < self.position_x+1 < 8 and 0 < self.position_y + 1 < 8:
            if self.side == 0 and (b[self.position_y+1][self.position_x+1] is not None
                                   and b[self.position_y+1][self.position_x+1].side != self.side):
                legal_moves.append((self.position_x+1, self.position_y+1))

        if 0 < self.position_x+1 < 8 and 0 < self.position_y+1 < 8:
            if self.side == 1 and (b[self.position_y-1][self.position_x-1] is not None
                                   and b[self.position_y-1][self.position_x-1].side != self.side):
                legal_moves.append((self.position_x-1, self.position_y-1))

        # Taking the other way
        if 0 < self.position_x+1 < 8 and 0 < self.position_y-1 < 8:
            if self.side == 0 and (b[self.position_y+1][self.position_x-1] is not None
                                   and b[self.position_y+1][self.position_x-1].side != self.side):
                legal_moves.append((self.position_x-1, self.position_y+1))

        if 0 < self.position_x-1 < 8 and 0 < self.position_y+1 < 8:
            if self.side == 1 and (b[self.position_y-1][self.position_x+1] is not None
                                   and b[self.position_y-1][self.position_x+1].side != self.side):
                legal_moves.append((self.position_x+1, self.position_y-1))

        return legal_moves

class Rook(ChessPiece):
    def __init__(self, position_x, position_y, side):
        moves = self.generate_moves()
        appearance = '♜' if side == 1 else '♖'
        super().__init__(position_x, position_y, moves, "Rook", side, appearance, 5)
    @staticmethod
    def generate_moves():
        moves = []
        for distance in range(-8, 9):
            moves.append((distance, 0))
            moves.append((0, distance))
        return moves

    def list_moves(self, board):
        legal_moves = []

        # Check "Downward"
        legal_moves.extend(self.check_range(1, 8, 0, 1, board))

        # Check "Upward"
        legal_moves.extend(self.check_range(1, 8, 0, -1, board))

        # Check "Left"
        legal_moves.extend(self.check_range(1, 8, 1, 0, board))

        # Check "Right"
        legal_moves.extend(self.check_range(1, 8, -1, 0, board))

        return legal_moves

class Knight(ChessPiece):
    def __init__(self, position_x, position_y, side):
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        appearance = '♞' if side == 1 else '♘'
        super().__init__(position_x, position_y, moves, "Knight", side, appearance, 3)

class Bishop(ChessPiece):
    def __init__(self, position_x, position_y, side):
        moves = self.generate_moves()
        appearance = '♝' if side == 1 else '♗'
        super().__init__(position_x, position_y, moves, "Bishop", side, appearance, 3)

    @staticmethod
    def generate_moves():
        moves = []
        move = 1
        for m in range(1, 9):
            moves.append((move, move))
            moves.append((-move, move))
            moves.append((move, -move))
            moves.append((-move, -move))
            move += 1
        return moves

    def list_moves(self, board):
        legal_moves = []

        # Check Up left
        legal_moves.extend(self.check_range(1, 8, 1, 1, board))

        #print(legal_moves)

        # Check Down left
        legal_moves.extend(self.check_range(1, 8, -1, -1, board))

        #print(legal_moves)

        # Check Down Right
        legal_moves.extend(self.check_range(1, 8, -1, 1, board))

        #print(legal_moves)

        # Check Up Right
        legal_moves.extend(self.check_range(1, 8, 1, -1, board))

        #print(legal_moves)

        return legal_moves

class Queen(ChessPiece):
    def __init__(self, position_x, position_y, side):
        moves = self.generate_moves()
        appearance = '♛' if side == 1 else '♕'
        super().__init__(position_x, position_y, moves, "Queen", side, appearance, 9)

    @staticmethod
    def generate_moves():
        moves = []
        move = 1
        for m in range(1, 9):
            moves.append((move, 0))
            moves.append((0, move))
            moves.append((move, move))
            moves.append((-move, move))
            moves.append((move, -move))
            moves.append((-move, -move))
            move += 1
        return moves

    def list_moves(self, board):
        legal_moves = []

        # Check Up left
        legal_moves.extend(self.check_range(1, 8, 1, 1, board))

        # Check Down left
        legal_moves.extend(self.check_range(1, 8, -1, -1, board))

        # Check Down Right
        legal_moves.extend(self.check_range(1, 8, -1, 1, board))

        # Check Up Right
        legal_moves.extend(self.check_range(1, 8, 1, -1, board))

        # Check "Downward"
        legal_moves.extend(self.check_range(1, 8, 0, 1, board))

        # Check "Upward"
        legal_moves.extend(self.check_range(1, 8, 0, -1, board))

        # Check "Left"
        legal_moves.extend(self.check_range(1, 8, 1, 0, board))

        # Check "Right"
        legal_moves.extend(self.check_range(1, 8, -1, 0, board))

        return legal_moves

class King(ChessPiece):
    def __init__(self, position_x, position_y, side):
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        appearance = '♚' if side == 1 else '♔'
        super().__init__(position_x, position_y, moves, "King", side, appearance, 10000)
