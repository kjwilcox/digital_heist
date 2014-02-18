#!/usr/bin/python3

import exhibition

import pygame
import logging
log = logging.getLogger(__name__)

TILE_SIZE = 32

class Map:
    
    def __init__(self, map_filename):
        self.cell = {}
        self.tile = {}
        log.info("loading map from: " + map_filename)
        
        with open(map_filename, encoding="utf8") as f:
            dimensions = f.readline().strip().split()
            self.width, self.height = int(dimensions[0]), int(dimensions[1])
            log.debug("height: {}, width: {}".format(self.height, self.width))
            
            for i in range(self.width):
                self.cell[i] = {}
                

            for y, line in enumerate(f):
                log.debug("{}".format(line.strip()))
                
                for x, cell in enumerate(line.strip().split()):
                    self.cell[x][y] = int(cell)
                    
            log.debug(self.cell)
        
        self.tile[0] = exhibition.images()["floor"]
        self.tile[1] = exhibition.images()["wall"]
                    
                    

    def render(self):
        
        screen = pygame.display.get_surface()
        
        for y in range(self.height):
            for x in range(self.width):
                screen.blit(self.tile[self.cell[x][y]],
                            (x*TILE_SIZE, y*TILE_SIZE))

