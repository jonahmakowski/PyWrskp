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