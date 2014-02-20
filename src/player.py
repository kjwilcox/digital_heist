#!/usr/bin/python3

import pygame
import collections

import exhibition
import inputdevice

class Player:
    
    def __init__(self, starting_position):
        self.pos = collections.namedtuple('position', ['x', 'y'])
        self.pos.x, self.pos.y = starting_position
        self.image = exhibition.images()["player"]
        self.vel = collections.namedtuple('Vector', ['x', 'y'])
        self.move_speed = 4.0
        
    def process_input(self, i):
        self.vel.x, self.vel.y = 0.0, 0.0

        if i.up:
            self.vel.y -= self.move_speed
        if i.down:
            self.vel.y += self.move_speed
        if i.left:
            self.vel.x -= self.move_speed
        if i.right:
            self.vel.x += self.move_speed
    
    def update(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        screen = pygame.display.get_surface()
        #screen.get_rect().clamp_ip(self.pos)
        
        
    def render(self, camera):
        screen = pygame.display.get_surface()
        screen.blit(self.image, (int(self.pos.x), int(self.pos.y)))
        
