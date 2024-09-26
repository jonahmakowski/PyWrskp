from board import Board
from peices import *

class Game:
    def __init__(self, board=None):
        self.move = 0
        self.board = Board() if board is None else board

    def move_pieces(self, piece:ChessPiece, location_cords:tuple, display=True):
        legal_moves = piece.list_moves(self.board)
        if location_cords not in legal_moves:
            return False
        if piece.side != self.move:
            return False
        self.board.move((piece.position_x, piece.position_y), location_cords)
        white_win, black_win = self.board.win_check()
        if display: self.board.pr()
        if white_win:
            print("White Wins!")
            exit()
        elif black_win:
            print("Black Wins!")
            exit()

        for piece in self.board.board[0]:
            if piece is not None and piece.name == "Pawn":
                self.board.promote(piece)

        for piece in self.board.board[-1]:
            if piece is not None and piece.name == "Pawn":
                self.board.promote(piece)

        self.move = 1 if self.move == 0 else 0
        return True

    def manual_move(self):
        print("It's {}'s move".format("White" if self.move == 0 else "Black"))
        while True:
            while True:
                piece_loc = input("Choose the piece you want to move: ")
                end_loc = input("Choose the end location: ")

                if piece_loc.isnumeric() and end_loc.isnumeric():
                    break
                print("Invalid input! Try again\n")

            if not self.move_pieces(self.board.get_location(int(piece_loc[0]), int(piece_loc[1])),
                                               (int(end_loc[0]), int(end_loc[1]))):
                print("That isn't a valid move for this piece, please try again.")
            else:
                break

    def copy(self, board=None):
        return self.__class__(board.copy() if board is not None else None)
