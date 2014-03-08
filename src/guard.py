#!/usr/bin/python3

import pygame

import direction
import exhibition
import random

class Guard:
    def __init__(self, pos, image):
        self.pos = pygame.Rect(pos,(32,32))
        self.image = image

    def render(self, camera):
        screen = pygame.display.get_surface()
        screen.blit(self.image, camera.world_to_screen(self.pos.topleft))
        
    def update(self):
        raise NotImplementedError
    

class RandomGhostGuard(Guard):
    
    def __init__(self, pos):
        super().__init__(pos, exhibition.images()["guard"])
    
    def update(self):
        if (random.random() > .4):
            d = random.choice([(0,1),(1,0),(0,-1),(-1,0)])
            x, y = d
            self.pos.x += x
            self.pos.y += y
