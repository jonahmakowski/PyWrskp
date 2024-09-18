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
        return self.__class__(self.position_x, self.position_y, self.side, self.value)

    def list_moves(self, board):
        legal_moves = []
        for move in self.moves:
            if not (self.position_x + move[0] < 0 or self.position_y + move[1] < 0):
                if board.get_location(self.position_x + move[0], self.position_y + move[1]) is None:
                    legal_moves.append((self.position_x + move[0], self.position_y + move[1]))
                elif board.get_location(self.position_x + move[0], self.position_y + move[1]).side != self.side:
                    legal_moves.append((self.position_x + move[0], self.position_y + move[1]))
        return legal_moves

    def check_range(self, start, end, x_mul, y_mul, b):
        moves = []
        direction = -1 if start > end else 1
        for distance in range(start, end, direction):
            #print('Checking {}, {} {}'.format(distance, self.position_x - distance*x_mul, self.position_y + distance*y_mul)) # Debug Message
            if self.position_x - distance*x_mul < 0 or self.position_y + distance*y_mul < 0:
                #print("Something was negative") # Debug Message
                break
            elif self.position_x - distance*x_mul > 7 or self.position_y + distance*y_mul > 7:
                #print('Something was above 7') # Debug Message
                break
            elif b.get_location(self.position_x - distance*x_mul, self.position_y + distance*y_mul) is None:
                moves.append((self.position_x - distance*x_mul, self.position_y + distance*y_mul))
                #print('Found empty location') # Debug Message
            elif b.get_location(self.position_x - distance*x_mul, self.position_y + distance*y_mul) is not None:
                if b.get_location(self.position_x - distance*x_mul, self.position_y + distance*y_mul).side != self.side:
                    moves.append((self.position_x - distance*x_mul, self.position_y + distance*y_mul))
                    #print('Found enemy location') # Debug Message
                    break
                elif b.get_location(self.position_x - distance*x_mul, self.position_y + distance*y_mul).side == self.side:
                    #print('Found friendly') # Debug Message
                    break
        #print('Function ended, returned {}'.format(moves)) # Debug Message
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
        if self.side == 0 and b[self.position_y+2][self.position_x] is None:
            legal_moves.append((self.position_x, self.position_y + 2))
        elif self.side == 1 and b[self.position_y-2][self.position_x] is None:
            legal_moves.append((self.position_x, self.position_y - 2))

        # Moving one forward
        if self.side == 0 and b[self.position_y+1][self.position_x] is None:
            legal_moves.append((self.position_x, self.position_y+1))
        elif self.side == 1 and b[self.position_y-1][self.position_x] is None:
            legal_moves.append((self.position_x, self.position_y-1))

        #Taking
        if self.side == 0 and (b[self.position_y+1][self.position_x+1] is not None
                               and b[self.position_y+1][self.position_x+1].side != self.side):
            legal_moves.append((self.position_x+1, self.position_y+1))
        elif self.side == 1 and (b[self.position_y-1][self.position_x-1] is not None
                                 and b[self.position_y-1][self.position_x-1].side != self.side):
            legal_moves.append((self.position_x-1, self.position_y-1))

        # Taking the other way
        if self.side == 0 and (b[self.position_y+1][self.position_x-1] is not None
                               and b[self.position_y+1][self.position_x-1].side != self.side):
            legal_moves.append((self.position_x-1, self.position_y+1))

        elif self.side == 1 and (b[self.position_y-1][self.position_x+1] is not None
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
        legal_moves.extend(self.check_range(-1, -9, 0, 1, board))

        # Check "Upward"
        legal_moves.extend(self.check_range(1, 9, 0, 1, board))

        # Check "Left"
        legal_moves.extend(self.check_range(1, 9, 1, 0, board))

        # Check "Right"
        legal_moves.extend(self.check_range(-1, -9, 1, 0, board))

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

        # Check Down left
        legal_moves.extend(self.check_range(-1, -8, 1, 1, board))

        # Check Down Right
        legal_moves.extend(self.check_range(-1, -8, -1, 1, board))

        # Check Up Right
        legal_moves.extend(self.check_range(1, 8, -1, 1, board))

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
        legal_moves.extend(self.check_range(-1, -8, 1, 1, board))

        # Check Down Right
        legal_moves.extend(self.check_range(-1, -8, -1, 1, board))

        # Check Up Right
        legal_moves.extend(self.check_range(1, 8, -1, 1, board))

        # Check "Downward"
        legal_moves.extend(self.check_range(-1, -9, 0, 1, board))

        # Check "Upward"
        legal_moves.extend(self.check_range(1, 9, 0, 1, board))

        # Check "Left"
        legal_moves.extend(self.check_range(1, 9, 1, 0, board))

        # Check "Right"
        legal_moves.extend(self.check_range(-1, -9, 1, 0, board))

        return legal_moves

class King(ChessPiece):
    def __init__(self, position_x, position_y, side):
        moves = [(1, 0), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        appearance = '♚' if side == 1 else '♔'
        super().__init__(position_x, position_y, moves, "King", side, appearance, 10000)
