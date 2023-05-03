import pygame
import random
# Create a list to store the objects
objects = []

# Initialize the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the gravity
GRAVITY = 0.0005

# Define the class for the objects in the game
class Object:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y += GRAVITY
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

# Main game loop
def Satisfying():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Create a new object when the mouse is clicked
                x, y = pygame.mouse.get_pos()
                size = random.randint(10, 50)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                objects.append(Object(x, y, size, color))

        # Clear the screen
        screen.fill((255, 255, 255))

        # Update and draw the objects
        for obj in objects:
            obj.update()

        pygame.display.update()

    pygame.quit()

