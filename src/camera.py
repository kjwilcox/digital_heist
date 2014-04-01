#!/usr/bin/python3

import pygame

import logging
log = logging.getLogger(__name__)


class Camera:
    pass


class PlayerCenteredCamera(Camera):
    """ A camera is a Rect that covers part (or all) of an area.
        It represents the screen's viewport into the world. """
        
    def __init__(self, player, _map):
        """ Creates a camera for the given map and player. """
        
        self.player = player
        self.map = _map
        self.rect = pygame.Rect(pygame.display.get_surface().get_rect())

    def update(self):
        """ Centers the camera on the player. """
        self.rect.center = self.player.rect.center
        self.rect.clamp_ip(self.map.bounds)

    def world_to_screen(self, coords):
        """ Converts world-space coordinates to screen-space coordinates based on the camera's position. """
        x, y = coords
        return x - self.rect.x, y - self.rect.y
