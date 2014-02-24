#!/usr/bin/python3

import pygame
import collections

import exhibition
import inputdevice
import direction
from data import PLAYER_SIZE, TILE_SIZE

class Player:
    
    def __init__(self, starting_position):
        self.pos = collections.namedtuple('position', ['x', 'y'])
        self.pos.x, self.pos.y = starting_position
        self.image = exhibition.images()["player"]
        self.vel = collections.namedtuple('vector', ['x', 'y'])
        self.dir = None
        self.vel.x, self.vel.y = 0.0, 0.0
        self.move_speed = 4.0
        self.fix_rect()

    def process_input(self, i):
        self.vel.x, self.vel.y = 0.0, 0.0

        d = self.dir
        if d in (direction.UP, None) and i.up:
            self.vel.y -= self.move_speed
            self.dir = direction.UP
            return
        
        if d in (direction.DOWN, None) and i.down:
            self.vel.y += self.move_speed
            self.dir = direction.DOWN
            return
        
        if d in (direction.LEFT, None) and i.left:
            self.vel.x -= self.move_speed
            self.dir = direction.LEFT
            return
        
        if d in (direction.RIGHT, None) and i.right:
            self.vel.x += self.move_speed
            self.dir = direction.RIGHT
            return
        
        self.dir = None
    
    def update(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        self.fix_rect()


    def fix_rect(self):
        self.rect = pygame.Rect(int(self.pos.x), int(self.pos.y), PLAYER_SIZE, PLAYER_SIZE)


    def render(self, camera):
        screen = pygame.display.get_surface()
        
        screen.blit(self.image, camera.world_to_screen((int(self.pos.x), int(self.pos.y))))
