import pygame
import time
import random
import sys
import os



pygame.init()



class Dino:
    def __init__(self):
        self.RED = (255,0,0)
        self.BLUE = (0, 0, 255)
        self.BLACK = (0, 0, 0)
        self.display = pygame.display.set_mode((400, 300))
        
        pygame.draw.rect(self.display, self.BLUE, pygame.Rect(90, 180, 60, 120))
        pygame.draw.rect(self.display, self.RED, pygame.Rect(30, 180, 60, 120))
        pygame.display.flip()
        
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.jump()
                
        
    def jump(self):
        y = 180
        while True:
            self.display.fill(self.BLACK)
            
            pygame.draw.rect(self.display, self.BLUE, pygame.Rect(90, y, 60, 120))
            pygame.draw.rect(self.display, self.RED, pygame.Rect(30, y, 60, 120))
            pygame.display.flip()
            
            y -= 1.5
            if y < 100:
                break
        
        while True:
            self.display.fill(self.BLACK)
            
            pygame.draw.rect(self.display, self.BLUE, pygame.Rect(90, y, 60, 120))
            pygame.draw.rect(self.display, self.RED, pygame.Rect(30, y, 60, 120))
            pygame.display.flip()
            
            y += 2
            time.sleep(0.001)
            if y == 175:
                break
            
        
        

Test = Dino()

