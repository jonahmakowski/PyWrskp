import pygame

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

board = [" " for x in range(9)]

font = pygame.font.Font(None, 36)

def draw_board(board):
  screen.fill(white)
  pygame.draw.line(screen, black, (166, 0), (166, 500), 4)
  pygame.draw.line(screen, black, (333, 0), (333, 500), 4)
  pygame.draw.line(screen, black, (0, 166), (500, 166), 4)
  pygame.draw.line(screen, black, (0, 333), (500, 333), 4)
  for i in range(9):
    text = font.render(board[i], True, black)
    text_rect = text.get_rect()
    if i < 3:
      text_rect.center = (62 + i * 166, 83)
    elif i < 6:
      text_rect.center = (62 + (i - 3) * 166, 249)
    else:
      text_rect.center = (62 + (i - 6) * 166, 415)
    screen.blit(text, text_rect)
  pygame.display.update()

def player_move(icon, x, y):
  if x < 166:
    column = 0
  elif x < 333:
    column = 1
  else:
    column = 2
  if y < 166:
    row = 0
  elif y < 333:
    row = 1
  else:
    row = 2
  position = row * 3 + column
  if board[position] == " ":
    board[position] = icon
  draw_board(board)

def is_victory(icon):
  if (board[0] == icon and board[1] == icon and board[2] == icon) or \
     (board[3] == icon and board[4] == icon and board[5] == icon) or \
     (board[6] == icon and board[7] == icon and board[8] == icon) or \
     (board[0] == icon and board[3] == icon and board[6] == icon) or \
     (board[1] == icon and board[4] == icon and board[7] == icon) or \
     (board[2] == icon and board[5] == icon and board[8] == icon) or \
     (board[0] == icon and board[4] == icon and board[8] == icon) or \
     (board[2] == icon and board[4] == icon and board[6] == icon):
    return True
  else:
    return False

def is_draw():
  if " " not in board:
    return True
  else:
    return False

draw_board(board)

running = True

turn = "X"

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      x, y = pygame.mouse.get_pos()
      player_move(turn, x, y)
      if is_victory(turn):
        print("Player " + turn + " wins!")
        running = False
      elif is_draw():
        print("It's a draw!")
        running = False
      if turn == "X":
        turn = "O"
      else:
        turn = "X"

pygame.quit()
