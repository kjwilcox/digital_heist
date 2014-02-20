#!/usr/bin/python3

import pygame

import exhibition

class Player:
    
    def __init__(self):
        self.pos = pygame.Rect((0,0),(32,32))
        self.image = exhibition.images()["player"]
        
    def render(self):
        screen = pygame.display.get_surface()
        screen.blit(self.image, self.pos)
