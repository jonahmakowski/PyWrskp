from board import Board
from peices import *

class Game:
    def __init__(self):
        self.move = 0
        self.board = Board()

    def move_pieces(self, piece:ChessPiece, location_cords:tuple):
        legal_moves = piece.list_moves(self.board)
        if location_cords not in legal_moves:
            return False
        self.board.move((piece.position_x, piece.position_y), location_cords)
        self.board.pr()
        white_win, black_win = self.board.win_check()
        if white_win:
            print("White Wins!")
            exit()
        elif black_win:
            print("Black Wins!")
            exit()
        self.board.pr()
        self.move = 1 if self.move == 0 else 0
        return True

    def manual_move(self):
        print("It's {}'s move".format("White" if self.move == 0 else "Black"))
        piece_loc = input("Choose the piece you want to move: ")
        end_loc = input("Choose the end location: ")

        if not (piece_loc.isnumeric() or end_loc.isnumeric()):
            exit()

        self.move_pieces(self.board.get_location(int(piece_loc[0]), int(piece_loc[1])),
                         (int(end_loc[0]), int(end_loc[1])))

t = Game()
t.board.pr()
while True:
    t.manual_move()
