from board import Board
from peices import *
from game import Game
from random import choice, randint

def artificial_unintelligence(game:Game):
    board = game.board
    my_pieces, _ = board.get_pieces()

    while True:
        piece = choice(my_pieces)
        if len(piece.list_moves(board)) != 0:
            break

    return piece, choice(piece.list_moves(board))

def get_pieces_and_moves(game:Game, side):
    board = game.board
    if side == 0:
        my_pieces, _ = board.get_pieces()
    else:
        _, my_pieces = board.get_pieces()
    moves = []
    for piece in my_pieces:
        moves.append(piece.list_moves(board))

    index = 0
    while True:
        if index == len(moves):
            break
        if not moves[index]:
            del moves[index]
            del my_pieces[index]
        else:
            index += 1

    return my_pieces, moves

def get_move_values(game:Game, my_pieces, moves, side):
    board = game.board

    move_values = []
    index = 0
    for move_series in moves:
        cur_series = []
        for move in move_series:
            copy = game.copy(board)
            copy.move_pieces(my_pieces[index], move, display=False)
            white, black = copy.board.calculate_points()
            value = white - black if side == 0 else black - white
            cur_series.append(value)
        move_values.append(cur_series)
        index += 1

    return move_values

def artificial_semi_intelligence(game:Game, side=0):
    my_pieces, moves = get_pieces_and_moves(game, side)

    #print('my_pieces', my_pieces)
    #print('moves', moves)

    move_values = get_move_values(game, my_pieces, moves, side)

    #print('move_values', move_values)

    largest_point_value = -100000000
    for move_series in move_values:
        for move_value in move_series:
            if move_value > largest_point_value:
                largest_point_value = move_value

    #print('largest_point_value', largest_point_value)

    best_moves = []
    index = 0
    for piece in my_pieces:
        m = 0
        for move in move_values[index]:
            if move == largest_point_value:
                best_moves.append({'piece': piece, 'move': moves[index][m]})
            m += 1
        index += 1

    #print('best_moves', best_moves)
    rand_index = 0 if len(best_moves) == 1 else randint(0, len(best_moves)-1)
    return best_moves[rand_index]['piece'], best_moves[rand_index]['move']

def make_move_into_game(game:Game, piece, move):
    #print('Line 89', game)
    g = game.copy()
    g.move_pieces(piece, move, display=False, override=True)
    return g

def m1_analyser(game:Game, piece, move, side):
    enemy_side = 1 if side == 1 else 0
    #print('line 96', game, piece, move)
    move_game = make_move_into_game(game, piece, move)
    opponent_best_piece, opponent_best_move = artificial_semi_intelligence(move_game, side=enemy_side)
    opponent_best = make_move_into_game(move_game, opponent_best_piece, opponent_best_move)
    white, black = opponent_best.board.calculate_points()
    return white - black if side == 0 else black - white, opponent_best

def bot_m1(game:Game, side=0):
    my_pieces, moves = get_pieces_and_moves(game, side)
    move_values = []
    move_games = []
    index = 0

    #print('Line 109', game)

    for move_series in moves:
        for move in move_series:
            #print('line 113', game, my_pieces[index], move, side)
            value, game = m1_analyser(game, my_pieces[index], move, side)
            move_values.append(value)
            move_games.append(game)
        index += 1

    highest = -1000000000
    index = 0
    for value in move_values:
        if value > highest:
            highest = value
            index = move_values.index(value)

    return move_games[index]
