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
        
    def test_render(self):
        screen = screen = pygame.display.get_surface()
        points = [self.rect.topleft, self.rect.topright,
                  self.rect.bottomright, self.rect.bottomleft]
        pygame.draw.lines(screen, (255,0,255), True, points)
        
    def world_to_screen(self, coords):
        """ Converts world-space coordinates to screen-space coordinates based on the camera. """
        x, y = coords
        return (x - self.rect.x, y - self.rect.y)
    
