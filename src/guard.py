#!/usr/bin/python3

import pygame

import direction
import exhibition
import random

import logging
log = logging.getLogger(__name__)


class Guard:
    """ A guard that patrols a level.
        Guard's posess a counter that limits how often they will stop to think.
        This represents a guard's reaction time, and planning capabilities. """
        
    def __init__(self, pos):
        self.pos = pygame.Rect(pos,(32,32))
        self.image = exhibition.images()["guard"]
        self.counter = random.randint(0, 60)
        self.counter_max = 60 # this means the guard will do planning once every 60 engine ticks

    def render(self, camera):
        screen = pygame.display.get_surface()
        screen.blit(self.image, camera.world_to_screen(self.pos.topleft))
        
    def update(self):
        self.counter += 1
        if self.counter > self.counter_max:
            self.counter = 0
            self.think()
            
        self.act()
    
    def think(self):
        #log.debug("{} is thinking".format(self))
        pass
    
    def act(self):
        pass
    




class PatrollingGuard(Guard):
    """ A guard that will patrol the given list of points.
        After moving to each point, it will start with the first point again.
        Points should be in world coordinates. """
        
    def __init__(self, points):
        self.points = points
        
    def get_next_point(self):
        """ Generator that returns the next point on the patrol path. """
        
        while True:
            for point in self.points:
                yield point
            
    
    

    

class RandomGhostGuard(Guard):
    
    def __init__(self, pos):
        super().__init__(pos)
    
    def act(self):
        if (random.random() > .4):
            d = random.choice([(0,1),(1,0),(0,-1),(-1,0)])
            x, y = d
            self.pos.x += x
            self.pos.y += y
