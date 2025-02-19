import pygame

DIS_WIDTH = 1280
DIS_HEIGHT = 820
pygame.init()
screen = pygame.display.set_mode([DIS_WIDTH, DIS_HEIGHT])
pygame.display.set_caption("Paint")

keep_going = True
mouse_down = False
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (131, 131, 131)
currentColour = RED
radius = 5

recWidth = int(DIS_WIDTH * 0.1)
recHeight = int(DIS_HEIGHT * 0.09)

redRectangle = pygame.Rect((0, 0), (recWidth, recHeight))
greenRectangle = pygame.Rect((recWidth, 0), (recWidth, recHeight))
blueRectangle = pygame.Rect(((recWidth * 2), 0), (recWidth, recHeight))

button_size = int(recHeight / 2)

max_radius = int(recHeight / 2)

topRectangle = pygame.Rect((0, 0), (DIS_WIDTH, recHeight))

increase = 5

plusRect_location_x = ((DIS_WIDTH - (max_radius * 4)))

buttonMinus = pygame.image.load('button_minus.png')
buttonPlus = pygame.image.load('button_plus.png')
buttonMinus = pygame.transform.scale(buttonMinus, (button_size, button_size))
buttonPlus = pygame.transform.scale(buttonPlus, ((button_size), button_size))
minusRect = buttonMinus.get_rect(topleft = (plusRect_location_x, button_size))
plusRect = buttonPlus.get_rect(topleft = (plusRect_location_x, 0))

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
        # get the current position of the mouse
        spot = pygame.mouse.get_pos()
        if redRectangle.collidepoint(spot):
            currentColour = RED
        elif greenRectangle.collidepoint(spot):
            currentColour = GREEN
        elif blueRectangle.collidepoint(spot):
            currentColour = BLUE
        else:
            # if it's not within a button, place a circle at the spot the mouse was pressed
            pygame.draw.circle(screen, currentColour, spot, radius)

    pygame.draw.rect(screen, GREY, topRectangle)
    pygame.draw.circle(screen, currentColour, (DIS_WIDTH - radius, radius), radius)
    pygame.draw.rect(screen, RED, redRectangle)
    pygame.draw.rect(screen, GREEN, greenRectangle)
    pygame.draw.rect(screen, BLUE, blueRectangle)
    screen.blit(buttonMinus, minusRect)
    screen.blit(buttonPlus, plusRect)
    pygame.display.update()

pygame.quit()