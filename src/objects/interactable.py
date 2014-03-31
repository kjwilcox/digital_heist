#!/usr/bin/python3

import pygame


class Interactable:
    """ A class representing an object that may be interacted with.
        This will include things like buttons, computers, and alarms. """

    def __init__(self, image, location, collision_rect, area):
        """ Creates an interactable object at the given location. """
        
        self.image = image
        self.rect = location
        self.collision_rect = collision_rect
        self.area = area
        self.enabled = True

    def render(self, camera):
        """ Renders the object if it has an image as is in the camera viewport. """
        
        if self.image and camera.rect.colliderect(self.rect):
            screen = pygame.display.get_surface()
            screen.blit(self.image, camera.world_to_screen(self.rect.topleft))

    def interact(self, interacter):
        """ Generic handler for interaction. """
        raise NotImplementedError
