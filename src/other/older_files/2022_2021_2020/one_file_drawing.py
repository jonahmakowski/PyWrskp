import pygame
pygame.init()

def which_color(x, radius, current_color, screen):
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
    if x < 750 and x >= 700:
        radius = 25
        return radius
    elif x >= 650:
        radius = 20
        return radius
    elif x >= 600:
        radius = 15
        return radius
    elif x >= 550:
        radius = 10
        return radius
    elif x >= 500:
        radius = 5
        return radius
    elif x >= 450:
        current_color = WHITE
        return current_color
    elif x >= 400:
        current_color = LIME
        return current_color
    elif x >= 350:
        current_color = ORANGE
        return current_color
    elif x >= 300:
        current_color = TEAL
        return current_color
    elif x >= 250:
        current_color = YELLOW
        return current_color
    elif x >= 200:
        current_color = PURPLE
        return current_color
    elif x >= 150:
        current_color = BLACK
        return current_color
    elif x >= 100:
        current_color = BLUE
        return current_color
    elif x >= 50:
        current_color = GREEN
        return current_color
    else:
        current_color = RED
        return current_color

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

current_background = BLACK

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
            pygame.draw.circle(screen, currentColour, spot, radius)
            pygame.display.update()
        elif y < 50 or x <= 750:
    
            temp = which_color(x, radius, currentColour, screen)
    
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
