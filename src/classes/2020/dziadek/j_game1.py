import pygame

keep_going = True
mouse_down = False
RED = (225, 0, 0)
radius = int(input('What would you like your pen size to be for this project?\n'))
current_color = (0,0,0)

pygame.init()
screen = pygame.display.set_mode([1290, 650])

pygame.display.set_caption('Click and drag to draw dots.')
WHITE = (225, 225, 225)
screen.fill(WHITE)

RED = (225, 0, 0)
red = pygame.Rect((0,0), (50,50))

GREEN = (0, 225, 0)
green = pygame.Rect((50, 0), (50,50))

BLUE = (0, 0, 225)
blue = pygame.Rect((100, 0), (50,50))

BLACK = (0, 0, 0)
black = pygame.Rect((150, 0), (50,50))

YELLOW = (225, 225, 3)
yellow = pygame.Rect((200, 0), (50,50))

white = pygame.Rect((250, 0), (50,50))

line = pygame.Rect((300, 0), (3, 50))

white_2 = pygame.Rect((303, 0), (50,50))

screen.fill(WHITE)
pygame.draw.rect(screen, RED, red)
pygame.draw.rect(screen, GREEN, green)
pygame.draw.rect(screen, BLUE, blue)
pygame.draw.rect(screen, BLACK, black)
pygame.draw.rect(screen, YELLOW, yellow)
pygame.draw.rect(screen, WHITE, white)
pygame.draw.rect(screen, BLACK, line)
pygame.draw.rect(screen, WHITE, white_2)

while keep_going:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keep_going = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_down = True

		if event.type == pygame.MOUSEBUTTONUP:
			mouse_down = False

		if mouse_down:
			spot = pygame.mouse.get_pos()
			x = spot[0]
			y = spot[1]
		
			if x < 50 and y <= 50:
				current_color = RED

			if (x >= 50 and x <= 100) and y <= 50:
				current_color = GREEN
			
			if (x >= 100 and x <= 150) and y <= 50:
				current_color = BLUE

			if (x >= 150 and x <= 200) and y <= 50:
				current_color = BLACK

			if (x >= 200 and x <= 250) and y <= 50:
				current_color = YELLOW

			if (x >= 250 and x <= 300) and y <= 50:
				current_color = WHITE
				screen.fill(WHITE)
				pygame.draw.rect(screen, RED, red)
				pygame.draw.rect(screen, GREEN, green)
				pygame.draw.rect(screen, BLUE, blue)
				pygame.draw.rect(screen, BLACK, black)
				pygame.draw.rect(screen, YELLOW, yellow)
				pygame.draw.rect(screen, WHITE, white)
				pygame.draw.rect(screen, BLACK, line)
				pygame.draw.rect(screen, WHITE, white_2)

			if (x >= 303 and x <= 353) and y <= 50:
				current_color = WHITE
		
			else: 
				pygame.draw.circle(screen, current_color, spot, radius)

	pygame.display.update()


pygame.quit()