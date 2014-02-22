#!/usr/bin/python3

import exhibition

import pygame
import logging
log = logging.getLogger(__name__)

from data import TILE_SIZE

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
                    
            self.bounds = pygame.Rect(0,0, self.width * TILE_SIZE, self.height * TILE_SIZE)
            log.debug("bounds: {}, {}".format(self.bounds.right, self.bounds.bottom))
                    
        
        self.tile[0] = exhibition.images()["floor"]
        self.tile[1] = exhibition.images()["wall"]
                    
                    

    def render(self, camera):
        
        screen = pygame.display.get_surface()
        
        camX = camera.rect.left
        camY = camera.rect.top
        
        """
        0 -> 0
        31 -> 0
        32 -> 1
        33 -> 1
        """
        
        
        start_x = camX // TILE_SIZE
        start_y = camY // TILE_SIZE
        
        offset_x = camX % TILE_SIZE
        offset_y = camY % TILE_SIZE
        
        end_x = camera.rect.right // TILE_SIZE
        end_y = camera.rect.bottom // TILE_SIZE
        
        
        for y in range(start_y, end_y + 1):
            for x in range(start_x, end_x + 1):
                #log.debug("<{},{}> at ({},{}) offset [{},{}]".format(
                #    x, y, x * TILE_SIZE - offset_x, y * TILE_SIZE - offset_y, offset_x, offset_y))
                screen.blit(self.tile[self.cell[x][y]],
                            (x * TILE_SIZE - offset_x,
                             y * TILE_SIZE - offset_y))






