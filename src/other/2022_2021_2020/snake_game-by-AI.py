import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (600, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Snake")

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set the clock
clock = pygame.time.Clock()

# Set the initial position of the snake
snake_position = [100, 100]

# Set the initial movement direction of the snake
snake_movement = [1, 0]

# Set the initial length of the snake
snake_body = [[100, 100], [90, 100], [80, 100]]

# Set the initial score
score = 0

# Set the initial apple position
apple_position = [300, 300]
apple_spawned = 1

# Set the game over flag
game_over = False

# Set the control keys
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Set the initial direction
direction = RIGHT

# Set the speed
speed = 10

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = UP
            elif event.key == pygame.K_RIGHT:
                direction = RIGHT
            elif event.key == pygame.K_DOWN:
                direction = DOWN
            elif event.key == pygame.K_LEFT:
                direction = LEFT
    
    # Update the snake position
    if direction == UP:
        snake_position[1] -= 10
    elif direction == RIGHT:
        snake_position[0] += 10
    elif direction == DOWN:
        snake_position[1] += 10
    elif direction == LEFT:
        snake_position[0] -= 10

    # Update the snake body
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == apple_position[0] and snake_position[1] == apple_position[1]:
        score += 1
        apple_spawned = 0
    else:
        snake_body.pop()
    
    if apple_spawned == 0:
        x_pos = random.randint(1, (window_size[0]-10)/10)
        y_pos = random.randint(1, (window_size[0]-10)/10)
        
    # Check for game over
    if snake_position[0] < 0 or snake_position[0] > window_size[0]-10 or snake_position[1] < 0 or snake_position[1] > window_size[1]-10:
       game_over = True
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over = True

    # Fill the screen with black
    screen.fill(black)

    # Draw the snake
    for position in snake_body:
        pygame.draw.rect(screen, white, pygame.Rect(position[0], position[1], 10, 10))

    # Draw the apple
    pygame.draw.rect(screen, white, pygame.Rect(apple_position[0], apple_position[1], 10, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(10)

# Print the final score
print("Your final score is: " + str(score))

