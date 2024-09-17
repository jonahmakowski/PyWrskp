class ChessPiece:
    def __init__(self, position_x, position_y, moves, name, side, appearance):
        self.position_x = position_x
        self.position_y = position_y
        self.name = name
        self.side = side # 0 is white, 1 is back
        self.moves = moves # Moves are formatted as tuples in a list, tuples should have x, y movement values for each
        self.appearance = appearance
    def move_to(self, board, position_x, position_y):
        pass
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
        raise ValueError

class Pawn(ChessPiece):
    def __init__(self, position_x, position_y, side):
        moves = [(0, 1)]
        appearance = '♟' if side == 1 else '♙'
        super().__init__(position_x, position_y, moves, "Pawn", side, appearance)

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
        super().__init__(position_x, position_y, moves, "Rook", side, appearance)

    @staticmethod
    def generate_moves():
        moves = []
        for distance in range(-8, 9):
            moves.append((distance, 0))
            moves.append((0, distance))
        return moves

class Knight(ChessPiece):
    def __init__(self, position_x, position_y, side):
        moves = [(3, 1), (3, -1), (-3, 1), (-3, -1), (1, 3), (-1, 3), (1, -3), (-1, -3)]
        appearance = '♞' if side == 1 else '♘'
        super().__init__(position_x, position_y, moves, "Knight", side, appearance)

class Bishop(ChessPiece):
    def __init__(self, position_x, position_y, side):
        moves = self.generate_moves()
        appearance = '♝' if side == 1 else '♗'
        super().__init__(position_x, position_y, moves, "Bishop", side, appearance)

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

class Queen(ChessPiece):
    def __init__(self, position_x, position_y, side):
        moves = self.generate_moves()
        appearance = '♛' if side == 1 else '♕'
        super().__init__(position_x, position_y, moves, "Queen", side, appearance)

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

class King(ChessPiece):
    def __init__(self, position_x, position_y, side):
        moves = [(1, 0), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        appearance = '♚' if side == 1 else '♔'
        super().__init__(position_x, position_y, moves, "King", side, appearance)
