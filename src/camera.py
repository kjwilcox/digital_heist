#!/usr/bin/python3

import pygame

import logging
log = logging.getLogger(__name__)

class Camera:
    def __init__(self, player, _map):
        self.player = player
        self.map = _map
        self.rect = pygame.Rect(pygame.display.get_surface().get_rect())
        
    def update(self):
        self.rect.center = self.player.rect.center
        self.rect.clamp_ip(self.map.bounds)
        
    def world_to_screen(self, coords):
        """ Converts world-space coordinates to screen-space coordinates based on the camera. """
        x, y = coords
        return (x - self.rect.x, y - self.rect.y)
    
