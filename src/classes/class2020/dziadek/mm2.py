import pygame

print('Based on Class_one1.py by Jonas, Apr 4, 2021; modified by Dziadek Marek.')

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (251, 0, 255)
YELLOW = (255, 247, 0)
TEAL = (0, 255, 255)
ORANGE = (255, 196, 0)
LIME = (132, 255, 0)

box_size = 50       # size (in pixels) of menu boxes
h_menu = box_size   # height of the menu bar (at top of the display)
colors = [BLACK, WHITE, RED, BLUE, GREEN, PURPLE, YELLOW, TEAL, ORANGE, LIME]
n_colors = len(colors)
pen_sizes = [5, 10, 15, 20, 25]
n_sizes = len(pen_sizes)
x_pixels = 1375
y_pixels = 750
currentColour = BLUE    # initial background color
radius = 10     # initial radius of the circle


def mk_menu():      # display menu boxes (colors and pen-sizes)
    global currentColour
    screen.fill(currentColour)
    x_cur = 0
    for col in colors:      # menu color boxes
        rectangle = pygame.Rect((x_cur, 0), (box_size, box_size))
        pygame.draw.rect(screen, col, rectangle)
        x_cur += box_size
    for pen in pen_sizes:      # menu pen-size boxes
        rectangle = pygame.Rect((x_cur, 0), (box_size, box_size))
        pygame.draw.rect(screen, BLACK, rectangle)
        pygame.draw.circle(screen, WHITE, (x_cur + box_size/2, box_size/2), pen)
        x_cur += box_size
    rectangle = pygame.Rect((x_cur, 0), (x_pixels, box_size))
    pygame.draw.rect(screen, WHITE, rectangle)
    pygame.display.update()


def mk_change(x_pos):      # change either color or pen_size
    global currentColour
    global radius
    x_org = x_pos
    colors_menu = n_colors * box_size
    if x_pos <= colors_menu:
        col_pos = int(x_pos / box_size)
        currentColour = colors[col_pos]
        # print('New color, pos = ' + str(col_pos))
        return
    pens_menu = n_sizes * box_size
    x_pos -= colors_menu
    if x_pos <= pens_menu:
        pen_pos = int(x_pos / box_size)
        radius = pen_sizes[pen_pos]
        # print('New radius, pos = ' + str(pen_pos))
    else:
        print('Ignore menu position: ' + str(x_org))


pygame.init()
screen = pygame.display.set_mode([x_pixels, y_pixels])
pygame.display.set_caption(
    "Click the color-square to change the current color; the space-bar changes the background color")
pygame.display.update()
mk_menu()
keep_going = True
mouse_down = False
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    # exit
            keep_going = False
        elif event.type == pygame.MOUSEBUTTONUP:    # do nothing
            mouse_down = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            spot = pygame.mouse.get_pos()   # get the current position of the mouse
            x = spot[0]
            y = spot[1]
            if y <= box_size:   # in menu area
                mk_change(x)     # change either color or pen-size
            else:
                mouse_down = True
        elif event.type == pygame.KEYDOWN:  # keyboard events
            if event.key == pygame.K_SPACE:   # only the space-bar handled
                screen.fill(currentColour)
                mk_menu()
                pygame.display.update()
        if mouse_down:
            spot = pygame.mouse.get_pos()  # get the current position of the mouse
            # print('Mouse position: ' + str(spot[0]) + ', ' + str(spot[1]))
            if spot[1] > box_size:
                margin = spot[1] - box_size
                paint_radius = radius
                if margin < radius:
                    paint_radius = margin
                pygame.draw.circle(screen, currentColour, spot, paint_radius)
                pygame.display.update()
            else:
                print('Painting in the menu-bar is suppressed.')

pygame.quit()
