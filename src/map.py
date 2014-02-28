#!/usr/bin/python3

import exhibition
import tile

import pygame
import logging
log = logging.getLogger(__name__)

from data import TILE_SIZE


class Map:
    """ The map class represents one map in the game.
        A map is made up of tiles, some of which may have collision properties. """
    
    
    def __init__(self, map_filename):
        """ Loads a map from the specified map file. """
        
        self.area = None
        self.tile = {}
        log.info("loading map from: " + map_filename)
        
        with open(map_filename, encoding="utf8") as f:
            dimensions = f.readline().strip().split()
            self.width, self.height = int(dimensions[0]), int(dimensions[1])
            log.debug("height: {}, width: {}".format(self.height, self.width))

            for y, line in enumerate(f):
                log.debug("{}".format(line.strip()))
                
                for x, cell in enumerate(line.strip().split()):
                    tile_num = int(cell)
                    tile_type = tile.tile_mapping[tile_num]
                    self.tile[x, y] = tile_type((x, y))
                    
            self.bounds = pygame.Rect(0,0, self.width * TILE_SIZE, self.height * TILE_SIZE)
            log.debug("bounds: {}, {}".format(self.bounds.right, self.bounds.bottom))
    

    def render(self, camera):
        """ Renders the map to the screen. """
        
        screen = pygame.display.get_surface()
        
        start_x = camera.rect.left // TILE_SIZE
        start_y = camera.rect.top // TILE_SIZE
        
        end_x = camera.rect.right // TILE_SIZE
        end_y = camera.rect.bottom // TILE_SIZE
        
        
        for y in range(start_y, min(end_y + 1, self.height)):
            for x in range(start_x, min(end_x + 1, self.width)):
                
                try:
                    t = self.tile[x, y]
                    t.render(camera)
                    
                except:
                    #log.error("tried to render non-existant tile ({}, {})".format(x, y))
                    continue
                
    def tile_to_world_coords(coords):
        x, y = coords
        return (x * TILE_SIZE, y * TILE_SIZE)
    






