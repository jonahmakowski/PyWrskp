import time
import json
import pygame
pygame.init()

class Main:
    def __init__(self, sprites=[], code=[], backdrops=[], variables=[], name=None):
        self.sprites = sprites
        self.backdrops = backdrops
        self.code = code
        self.screen = 'load'
        self.display = {}
        self.variables = variables
    
    def save(self):
        with open(self.name+'.txt', 'w') as f:
            for item in self.code:
                f.write(json.dumps(item) + '\n')
    def load(self, name):
        with open(name+'.txt') as f:
            lines = f.readlines()

        self.code = []
        for line in lines:
            self.code.append(json.loads(line))
        self.name = name