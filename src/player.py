#!/usr/bin/python3

import pygame
import collections

import exhibition
import inputdevice

class Player:
    
    def __init__(self):
        self.pos = pygame.Rect((0,0),(32,32))
        self.image = exhibition.images()["player"]
        self.vel = collections.namedtuple('Vector', ['x', 'y'])
        self.move_speed = 4
        
    def render(self):
        screen = pygame.display.get_surface()
        screen.blit(self.image, self.pos)
        
    def process_input(self, i):
        self.vel.x = 0
        self.vel.y = 0
        if i.up:
            self.vel.y -= 1
        if i.down:
            self.vel.y += 1
        if i.left:
            self.vel.x -= 1
        if i.right:
            self.vel.x += 1
    
    def update(self):
        self.pos.x += self.vel.x * self.move_speed
        self.pos.y += self.vel.y * self.move_speed
        screen = pygame.display.get_surface()
        #screen.get_rect().clamp_ip(self.pos)
        
