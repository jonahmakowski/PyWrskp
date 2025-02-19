import pygame
import time
import random

pygame.init()

class Dino:
    def __init__(self):
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.BLACK = (0, 0, 0)
        self.display = pygame.display.set_mode((400, 300))
        
        pygame.draw.rect(self.display, self.BLUE, pygame.Rect(90, 175, 60, 120))
        pygame.draw.rect(self.display, self.RED, pygame.Rect(30, 175, 60, 120))
        pygame.display.flip()
        
        time.sleep(1)
        
        self.jump()
        
    def jump(self):
        y = 175
        while True:
            self.display.fill(self.BLACK)
            
            pygame.draw.rect(self.display, self.BLUE, pygame.Rect(90, y, 60, 120))
            pygame.draw.rect(self.display, self.RED, pygame.Rect(30, y, 60, 120))
            pygame.display.flip()
            
            y -= 1
            if y < 100:
                break
        
        while True:
            self.display.fill(self.BLACK)
            
            pygame.draw.rect(self.display, self.BLUE, pygame.Rect(90, y, 60, 120))
            pygame.draw.rect(self.display, self.RED, pygame.Rect(30, y, 60, 120))
            pygame.display.flip()
            
            y += 1
            time.sleep(0.01)
            if y == 175:
                break
        

Test = Dino()
