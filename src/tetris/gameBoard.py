from pieces import *
from random import randint
import keyboard

GRID_WIDTH = 10
GRID_HEIGHT = 20
PIECE_SPAWN = (3, 0)

class Board:
    def __init__(self):
        self.piece_queue = [randint(0, 6) for _ in range(3)]
        self.board = self.generate_board().copy()
        self.active_piece = None
        self.refresh_amount = 0
    
    @staticmethod
    def generate_board():
        row = [0 for _ in range(GRID_WIDTH)]
        result = []
        for _ in range(GRID_HEIGHT):
            result.append(row.copy())
        
        return result.copy()
    
    def overlay_piece(self):
        if self.active_piece is None:
            raise ValueError('Active Piece is None')
        
        overlay_board = [row.copy() for row in self.board]
        locations = self.active_piece.extrapolate_positions().copy()

        for row in locations:
            for data in row:
                if data['value'] != 0:
                    overlay_board[data.copy()['pos'][1]][data.copy()['pos'][0]] = 2
        
        return overlay_board.copy()
    
    def display_board(self):
        if self.active_piece is None:
            for row in self.board: print(*row.copy())
        else:
            overlay_board = self.overlay_piece().copy()
            for row in overlay_board: print(*row.copy())
    
    def generate_new_piece(self):
        ind = self.piece_queue[0]
        self.piece_queue.pop(0)
        self.piece_queue.append(randint(0, 6))
        
        match ind:
            case 0:
                self.active_piece = Piece0(PIECE_SPAWN)
            case 1:
                self.active_piece = Piece1(PIECE_SPAWN)
            case 2:
                self.active_piece = Piece2(PIECE_SPAWN)
            case 3:
                self.active_piece = Piece3(PIECE_SPAWN)
            case 4:
                self.active_piece = Piece4(PIECE_SPAWN)
            case 5:
                self.active_piece = Piece5(PIECE_SPAWN)
            case 6:
                self.active_piece = Piece6(PIECE_SPAWN)

    def perform_refresh(self):
        self.refresh_amount += 1
        print('Refresh {}'.format(self.refresh_amount))
        if self.active_piece == None:
            self.generate_new_piece()
        self.display_board()
        self.active_piece.move_down()
        if keyboard.is_pressed('left_arrow'):
            print('Pressed')

test = Board()
#test.display_board()

test.perform_refresh()
test.perform_refresh()
