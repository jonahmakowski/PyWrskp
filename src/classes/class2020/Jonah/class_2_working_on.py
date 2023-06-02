import pygame

DIS_WIDTH = 1280
DIS_HEIGHT = 820
pygame.init()
screen = pygame.display.set_mode([DIS_WIDTH, DIS_HEIGHT])
pygame.display.set_caption("Paint")

buttonMinus = pygame.image.load('button_minus.png')
buttonPlus = pygame.image.load('button_plus.png')

keep_going = True
mouse_down = False
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (131, 131, 131)
currentColour = RED
radius = 5

colors = [RED, GREEN, BLUE]
buttons = [buttonMinus, buttonPlus]

recWidth = int(DIS_WIDTH * 0.1)
recHeight = int(DIS_HEIGHT * 0.09)

button_size = int(recHeight / 2)

max_radius = int(recHeight / 2)
location_x = ((DIS_WIDTH - (max_radius * 4)))

def menu():
    global location_x
    global button_size
    global colors
    topRectangle = pygame.Rect((0, 0), (DIS_WIDTH, recHeight))
    pygame.draw.rect(screen, GREY, topRectangle)
    pygame.draw.circle(screen, currentColour, (DIS_WIDTH - radius, radius), radius)
    x = 0
    for col in colors:
        rectangle = pygame.Rect((x, 0), (recWidth, recHeight))
        pygame.draw.rect(screen, col, rectangle)
        x += recWidth
    y = 0
    for button in buttons:
        plus_minus = pygame.transform.scale(button, (button_size, button_size))
        plus_minus_rec = plus_minus.get_rect(topleft = (location_x, y))
        screen.blit(plus_minus, plus_minus_rec)
        y += button_size
    pygame.display.update()
    
def check_color():
    global colors
    global recWidth
    global currentColour
    x = 0
    spot = pygame.mouse.get_pos()
    for col in colors:
        rectangle = pygame.Rect((x, 0), (recWidth, recHeight))
        x += recWidth
        if rectangle.collidepoint(spot):
            return 'color'
    for button in buttons:
        plus_minus = pygame.transform.scale(button, (button_size, button_size))
        plus_minus_rec = plus_minus.get_rect(topleft = (location_x, y))
        y += button_size
        if plus_minus_rec.collidepoint(spot):
            return 'radius'
    return False

def check():
    global colors
    global recWidth
    global currentColour
    global recHeight
    global radius
    x = 0
    spot = pygame.mouse.get_pos()
    for col in colors:
        rectangle = pygame.Rect((x, 0), (recWidth, recHeight))
        x += recWidth
        if rectangle.collidepoint(spot):
            currentColour = col

increase = 5

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            spot = pygame.mouse.get_pos()
            if minusRect.collidepoint(spot):
                if radius > increase:
                    radius -= increase
            if plusRect.collidepoint(spot):
                if radius < max_radius:
                    radius += increase
                    if radius > max_radius:
                        radius -= increase
            else:
                mouse_down = True

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(BLACK)
            if event.key == pygame.K_r:
                radius = 5
            if event.key == pygame.K_q:
                if radius < max_radius:
                    radius += increase
                    if radius > max_radius:
                        radius -= increase
            if event.key == pygame.K_a:
                if radius > increase:
                    radius -= increase
            if event.key == pygame.K_z:
                screen.fill(currentColour)

    if mouse_down:
        # if the event is pressing the mouse
        if not check_color():
            # if it's not within a button, place a circle at the spot the mouse was pressed
            pygame.draw.circle(screen, currentColour, spot, radius)
    menu()

pygame.quit()