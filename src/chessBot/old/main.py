import helper

board = helper.ChessBoard()

test = helper.ChessBoard(board=[['2A', '3A', '4A', '5A', '6A', '4A', '3A', '2A'],
                                ['1A', '1A', '1A', '1A', '1A', '1A', '1A', '1A'],
                                ['00', '00', '00', '00', '00', '00', '00', '00'],
                                ['00', '00', '00', '00', '00', '00', '00', '00'],
                                ['00', '00', '00', '00', '5A', '00', '00', '00'],
                                ['00', '00', '00', '00', '00', '00', '00', '00'],
                                ['1B', '1B', '1B', '1B', '00', '1B', '1B', '1B'],
                                ['2B', '3B', '4B', '5B', '6B', '4B', '3B', '2B']])

test.display_board()
print(test.check('B'))

raise Exception

bot = helper.Bot(3)
while True:
    board.display_board()
    board.move(int(input("The Piece's current x pos  ")),
               int(input("The Piece's current y pos  ")),
               int(input("The x pos of where you want to move it  ")),
               int(input("The y pos of where you want to move it  ")))
    board.display_board()
    board = bot.calculate_moves(board.clone())
