#!/usr/bin/python3

import pygame
import collections

import exhibition
import inputdevice
import direction
from data import PLAYER_SIZE, TILE_SIZE

import logging
log = logging.getLogger(__name__)

class Player:
    """ The player class represents a character controlled by the player.
        There may be multiple player instances, but generally only one is
        active and recieving inputs at any given time. """
    
    
    def __init__(self, starting_position):
        """ Creates a player at the specified (x, y) starting position. """
        
        self.area = None
        self.pos = collections.namedtuple('position', ['x', 'y'])
        self.pos.x, self.pos.y = starting_position
        self.image = exhibition.images()["player"]
        self.vel = collections.namedtuple('vector', ['x', 'y'])
        self.dir = None
        self.vel.x, self.vel.y = 0.0, 0.0
        self.move_speed = 4.0
        self.fix_rect()
        
    def __str__(self):
        return "<Player {}>".format(self.rect.topleft)


    def process_input(self, i):
        """ Modifies player's velocity based on given input device i. """
        
        self.vel.x, self.vel.y = 0.0, 0.0
        d = self.dir
        self.dir = None
        
        if i.A:
            if self.attempt_interact():
                return
        

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
    
    
    def update(self):
        """ Updates position and snaps player to grid. """
        
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        self.fix_rect()


    def fix_rect(self):
        """ Sets rectangle used for rendering and collision to integer coordinates. """
        
        self.rect = pygame.Rect(int(self.pos.x), int(self.pos.y), PLAYER_SIZE, PLAYER_SIZE)
        self.collision_rect = pygame.Rect(0,0,14,14) # size of the player's feet
        self.collision_rect.midbottom = self.rect.midbottom


    def fix_pos(self):
        """ Sets the position to reflect the position of the rects. Used in collisions. """
        self.rect.midbottom = self.collision_rect.midbottom
        self.pos.x, self.pos.y = float(self.rect.x), float(self.rect.y)


    def render(self, camera):
        """ Renders player character on screen. """
        
        screen = pygame.display.get_surface()
        screen.blit(self.image, camera.world_to_screen((int(self.pos.x), int(self.pos.y))))


    def attempt_interact(self):
        log.debug("attempting collision")
        
        collision = None
        
        for k, v in self.area.interactables.items():
            if v.collision_rect.colliderect(self.collision_rect):
                collision = v
                break
        
        if collision != None:
            collision.interact(self)
            

