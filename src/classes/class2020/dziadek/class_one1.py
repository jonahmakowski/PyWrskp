import pygame

print('version 1')

pygame.init()
screen = pygame.display.set_mode([1375, 750])
pygame.display.set_caption(
    "Click the color-square to change the current color; the space-bar changes the background color")

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

currentColour = BLUE
screen.fill(currentColour)
pygame.display.update()
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

dotRectangle5 = pygame.Rect((500, 0), (50, 50))
dotRectangle10 = pygame.Rect((550, 0), (50, 50))
dotRectangle15 = pygame.Rect((600, 0), (50, 50))
dotRectangle20 = pygame.Rect((650, 0), (50, 50))
dotRectangle25 = pygame.Rect((700, 0), (50, 50))

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
        elif x < 50:
            # if the current position is within the red square, change the colour to red
            currentColour = RED
        elif x < 100:
            # if the current position is within the green square, change the colour to green
            currentColour = GREEN
        elif x < 150:
            # if the current position is within the blue square, change the colour to blue
            currentColour = BLUE
        elif x < 200:
            # if the current position is within the black square, change the colour to black
            currentColour = BLACK
        elif x < 250:
            # if the current position is within the purple square, change the colour to purple
            currentColour = PURPLE
        elif x < 300:
            # if the current position is within the yellow square, change the colour to yellow
            currentColour = YELLOW
        elif x < 350:
            # if the current position is within the teal square, change the colour to teal
            currentColour = TEAL
        elif x < 400:
            # if the current position is within the orange square, change the colour to orange
            currentColour = ORANGE
        elif x < 450:
            # if the current position is within the lime square, change the colour to lime
            currentColour = LIME
        elif x < 500:
            # if the current position is within the white square, change the colour to white
            currentColour = WHITE
        elif x < 550:
            # if touching the small circle change pensize to 5
            radius = 5
        elif x < 600:
            # if touching the small circle change pensize to 10
            radius = 10
        elif x < 650:
            # if touching the small circle change pensize to 15
            radius = 15
        elif x < 700:
            # if touching the small circle change pensize to 20
            radius = 20
        elif x < 750:
            # if touching the small circle change pensize to 25
            radius = 25

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
    # pygame.display.update()a   # not needed
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
