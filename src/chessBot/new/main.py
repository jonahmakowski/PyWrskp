from board import Board
from peices import *
from bot import *
from game import Game

def player_mainloop():
    g = Game()
    g.board.pr()
    while True:
        g.manual_move()

def artificial_unintelligence_mainloop():
    g = Game()
    while True:
        piece, location = artificial_unintelligence(g)
        g.move_pieces(piece, location)
        g.manual_move()

def artificial_semi_intelligence_mainloop():
    g = Game()
    while True:
        piece, location = artificial_semi_intelligence(g)
        g.move_pieces(piece, location)
        g.manual_move()

def m1_mainloop():
    g = Game()
    while True:
        g = bot_m1(g, 0)
        g.manual_move()

artificial_semi_intelligence_mainloop()
