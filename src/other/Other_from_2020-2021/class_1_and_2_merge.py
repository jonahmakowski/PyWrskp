# here I defined my "which_color" fuction:

def which_color(x, radius, current_color):
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
    if dotRectangle25.collidepoint(spot):
        radius = 25
        return radius
    elif dotRectangle20.collidepoint(spot):
        radius = 20
        return radius
    elif dotRectangle15.collidepoint(spot):
        radius = 15
        return radius
    elif dotRectangle10.collidepoint(spot):
        radius = 10
        return radius
    elif dotRectangle5.collidepoint(spot):
        radius = 5
        return radius
    elif whiteRectangle.collidepoint(spot):
        current_color = WHITE
        return current_color
    elif limeRectangle.collidepoint(spot):
        current_color = LIME
        return current_color
    elif orangeRectangle.collidepoint(spot):
        current_color = ORANGE
        return current_color
    elif tealRectangle.collidepoint(spot):
        current_color = TEAL
        return current_color
    elif yellowRectangle.collidepoint(spot):
        current_color = YELLOW
        return current_color
    elif purpleRectangle.collidepoint(spot):
        current_color = PURPLE
        return current_color
    elif blackRectangle.collidepoint(spot):
        current_color = BLACK
        return current_color
    elif blueRectangle.collidepoint(spot):
        current_color = BLUE
        return current_color
    elif greenRectangle.collidepoint(spot):
        current_color = GREEN
        return current_color
    elif redRectangle.collidepoint(spot):
        current_color = RED
        return current_color

# here we start with pygame:

import pygame

pygame.init()
screen = pygame.display.set_mode([1375,750])
pygame.display.set_caption("Paint")

keep_going = True
mouse_down = False

# defines colors
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

currentColour = (0, 0, 0)
radius = 10

# defines rectangles
redRectangle = pygame.Rect((0, 0), (50, 50))
greenRectangle = pygame.Rect((50, 0), (50, 50))
blueRectangle = pygame.Rect((100, 0), (50, 50))
blackRectangle = pygame.Rect((150, 0), (50, 50))
purpleRectangle = pygame.Rect((200, 0), (50, 50))
yellowRectangle = pygame.Rect((250, 0), (50, 50))
tealRectangle = pygame.Rect((300, 0), (50, 50))
orangeRectangle = pygame.Rect((350, 0), (50, 50))
limeRectangle = pygame.Rect((400, 0), (50, 50))
whiteRectangle = pygame.Rect((450, 0), (50, 50))

dotRectangle5 = pygame.Rect((500, 0), (50,50))
dotRectangle10 = pygame.Rect((550, 0), (50,50))
dotRectangle15 = pygame.Rect((600, 0), (50,50))
dotRectangle20 = pygame.Rect((650, 0), (50,50))
dotRectangle25 = pygame.Rect((700, 0), (50,50))

eraser = BLACK

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(currentColour)
                current_background = currentColour
                eraser = currentColour
                pygame.display.update()
            if event.key == pygame.K_a:
                screen.fill(current_background)
                pygame.display.update()

    if mouse_down:
        # if the event is pressing the mouse
        # get the current position of the mouse
        spot = pygame.mouse.get_pos()
        x = spot[0]
        y = spot[1]
        if y > 50 or x >= 750:
            if currentColour == eraser:
                pygame.draw.circle(screen, currentColour, spot, radius * 2)
                pygame.display.update()
            if currentColour != eraser:
                pygame.draw.circle(screen, currentColour, spot, radius)
                pygame.display.update()
        elif y < 50 or x <= 750:
        
            temp = which_color(x, radius, currentColour)
        
            temp_true = isinstance(temp, int)
        
            if temp_true == True:
                radius = temp
        
            elif temp_true == False:
                if temp != None:
                    currentColour = temp
    # draws rectangles
    pygame.draw.rect(screen, RED, redRectangle)
    pygame.draw.rect(screen, GREEN, greenRectangle)
    pygame.draw.rect(screen, BLUE, blueRectangle)
    pygame.draw.rect(screen, BLACK, blackRectangle)
    pygame.draw.rect(screen, PURPLE, purpleRectangle)
    pygame.draw.rect(screen, YELLOW, yellowRectangle)
    pygame.draw.rect(screen, TEAL, tealRectangle)
    pygame.draw.rect(screen, ORANGE, orangeRectangle)
    pygame.draw.rect(screen, LIME, limeRectangle)
    pygame.draw.rect(screen, WHITE, whiteRectangle)
    pygame.display.update()
    pygame.draw.rect(screen, BLACK, dotRectangle5)
    pygame.draw.rect(screen, BLACK, dotRectangle10)
    pygame.draw.rect(screen, BLACK, dotRectangle15)
    pygame.draw.rect(screen, BLACK, dotRectangle20)
    pygame.draw.rect(screen, BLACK, dotRectangle25)
    # draws circles
    pygame.draw.circle(screen, WHITE, (525, 25), 5)
    pygame.draw.circle(screen, WHITE, (575, 25), 10)
    pygame.draw.circle(screen, WHITE, (625, 25), 15)
    pygame.draw.circle(screen, WHITE, (675, 25), 20)
    pygame.draw.circle(screen, WHITE, (725, 25), 25)
    pygame.display.update()

pygame.quit()
