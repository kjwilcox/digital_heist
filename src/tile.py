#!/usr/bin/python3

import exhibition
from data import TILE_SIZE

import pygame
import collections
import logging
log = logging.getLogger(__name__)


class Tile:
    def __init__(self, pos):
        self.tile_pos = pos
        x, y = pos
        self.rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.collision_rect = None
        
    def render(self, camera):
        screen = pygame.display.get_surface()
        screen.blit(self.image, camera.world_to_screen(self.rect.topleft))


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
    
tile_mapping = collections.defaultdict(MissingTile, {0: FloorTile, 1: WallTile})
