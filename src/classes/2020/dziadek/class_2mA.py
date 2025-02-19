import pygame

# definitions of the available colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (131, 131, 131)

# definitions of available buttons
buttonMinus = pygame.image.load('button_minus.png')
buttonPlus = pygame.image.load('button_plus.png')

# definitions of lists of currently used pen-colors and buttons
colors = [RED, GREEN, BLUE]
buttons = [buttonMinus, buttonPlus]

#  dimensions and sizes used
DIS_WIDTH = 1280
DIS_HEIGHT = 820
recWidth = int(DIS_WIDTH * 0.1)
recHeight = int(DIS_HEIGHT * 0.09)
button_size = int(recHeight / 2)
max_radius = int(recHeight / 2)
min_radius = 5
button_x = int((DIS_WIDTH - (max_radius * 4)))
radius_change = 5       # increase/decrease of radius through -/+ buttons
ini_radius = 15  # initial/default radius

# initialize
currentColour = colors[0]
radius = ini_radius
pygame.init()
screen = pygame.display.set_mode([DIS_WIDTH, DIS_HEIGHT])
pygame.display.set_caption("Paint")


def menu():     # display rectangles with pen-colors and buttons to change the radius
    # global button_size
    # global colors
    menu_bar = pygame.Rect((0, 0), (DIS_WIDTH, recHeight))
    pygame.draw.rect(screen, GREY, menu_bar)
    x = 0   # current x position
    y = 0   # current y position
    for col in colors:      # draw rectangles for changing the pen color
        rectangle = pygame.Rect((x, y), (recWidth, recHeight))
        pygame.draw.rect(screen, col, rectangle)
        x += recWidth
    for button in buttons:      # draw button for decreasing/increasing the pen size
        plus_minus = pygame.transform.scale(button, (button_size, button_size))
        plus_minus_rec = plus_minus.get_rect(topleft=(button_x, y))
        screen.blit(plus_minus, plus_minus_rec)
        y += button_size
    pygame.draw.circle(screen, currentColour, (DIS_WIDTH - int(1.5 * max_radius), int(recHeight/2)), radius)
    pygame.display.update()


def change_pen():   # returns True if the pen (color or size) was changed, otherwise returns False
    # global colors
    global recWidth
    global currentColour
    global button_x
    # global spot
    global radius
    x = 0
    y = 0
    for col in colors:
        rectangle = pygame.Rect((x, 0), (recWidth, recHeight))
        x += recWidth
        if rectangle.collidepoint(spot):
            currentColour = col
            menu()      # need to be repainted for the changed pen color
            return True
    is_first = True
    for button in buttons:
        plus_minus = pygame.transform.scale(button, (button_size, button_size))
        plus_minus_rec = plus_minus.get_rect(topleft=(button_x, y))
        if plus_minus_rec.collidepoint(spot):
            if is_first:    # decrease the radius for the first/top button
                radius -= radius_change
                if radius < min_radius:
                    radius = min_radius
            else:    # increase the radius for the second/bottom button
                radius += radius_change
                if radius > max_radius:
                    radius = max_radius
            menu()      # need to be repainted for the changed pen size
            return True
        y += button_size
        is_first = False
    return False


# processing mouse events
menu()
keep_going = True
mouse_down = False
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            spot = pygame.mouse.get_pos()
            if change_pen():
                mouse_down = False
            else:
                mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(BLACK)
            elif event.key == pygame.K_z:       # change the canvas background to the current color
                screen.fill(currentColour)
            elif event.key == pygame.K_r:       # reset the radius to the initial value
                radius = ini_radius
            elif event.key == pygame.K_i:       # increase the radius size (same as through the + button)
                radius += radius_change
                if radius > max_radius:
                    radius = max_radius
            elif event.key == pygame.K_d:       # decrease the radius size (same as through the - button)
                radius -= radius_change
                if radius < min_radius:
                    radius = min_radius
            menu()      # repaint menu (for possibly changed pen-size or color)

    if mouse_down:   # mouse not pointing to menu
        spot = pygame.mouse.get_pos()
        if spot[1] > recHeight:     # mouse in the painting area
            margin = spot[1] - recHeight
            paint_radius = radius
            if margin < radius:     # paint only below the menu bar
                paint_radius = margin
            else:
                paint_radius = radius
            pygame.draw.circle(screen, currentColour, spot, paint_radius)
            pygame.display.update()

pygame.quit()
