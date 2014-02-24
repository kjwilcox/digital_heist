#!/usr/bin/python3

import pygame
import collections

import exhibition
import inputdevice
from direction import Direction
from data import PLAYER_SIZE, TILE_SIZE

class Player:
    
    def __init__(self, starting_position):
        self.pos = collections.namedtuple('position', ['x', 'y'])
        self.pos.x, self.pos.y = starting_position
        self.rect = pygame.Rect(starting_position, (PLAYER_SIZE, PLAYER_SIZE))
        self.image = exhibition.images()["player"]
        self.vel = collections.namedtuple('vector', ['x', 'y'])
        self.dir = None
        self.vel.x, self.vel.y = 0.0, 0.0
        self.move_speed = 4.0
        
    def process_input(self, i):
        self.vel.x, self.vel.y = 0.0, 0.0

        d = self.dir
        if d in (Direction.UP, None) and i.up:
            self.vel.y -= self.move_speed
            self.dir = Direction.UP
            return
        
        if d in (Direction.DOWN, None) and i.down:
            self.vel.y += self.move_speed
            self.dir = Direction.DOWN
            return
        
        if d in (Direction.LEFT, None) and i.left:
            self.vel.x -= self.move_speed
            self.dir = Direction.LEFT
            return
        
        if d in (Direction.RIGHT, None) and i.right:
            self.vel.x += self.move_speed
            self.dir = Direction.RIGHT
            return
        
        self.dir = None
    
    def update(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        
        self.rect = pygame.Rect(int(self.pos.x), int(self.pos.y), PLAYER_SIZE, PLAYER_SIZE)
        
        
    def render(self, camera):
        screen = pygame.display.get_surface()
        
        screen.blit(self.image, camera.world_to_screen((int(self.pos.x), int(self.pos.y))))
        
