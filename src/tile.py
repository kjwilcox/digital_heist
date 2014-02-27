#!/usr/bin/python3

import exhibition
from data import TILE_SIZE

import pygame
import collections
import logging
log = logging.getLogger(__name__)


class Tile:
    """ A tile represents one tile in an area's map.
        It has an image, a position rectangle, and an optional collision rectangle.
        An abstract base class. Child classes must define an image."""
        
        
    def __init__(self, pos):
        """ Initializes a tile with position. No image or collision rect set. """
        
        self.tile_pos = pos
        x, y = pos
        self.rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.collision_rect = None
        
        
    def render(self, camera):
        """ Renders the map tile to the screen using the provided camera. """
        
        screen = pygame.display.get_surface()
        screen.blit(self.image, camera.world_to_screen(self.rect.topleft))


##################################

class FloorTile(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = exhibition.images()["floor"]



class WallTile(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.collision_rect = self.rect
        self.image = exhibition.images()["wall"]
    
    
    
class MissingTile(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = exhibition.images()["missing"]
        log.error("Missing tile created at {}, {}".format(pos[0], pos[1]))
 
 
# This tile mapping maps the integers in the map file format to the appropriate tile types.
# This dictionary IS the file format for the map.
tile_mapping = collections.defaultdict(MissingTile, {0: FloorTile, 1: WallTile})
