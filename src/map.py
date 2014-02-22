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
        self.tile[-1] = exhibition.images()["missing"]
                    
                    

    def render(self, camera):
        
        screen = pygame.display.get_surface()
        
        start_x = camera.rect.left // TILE_SIZE
        start_y = camera.rect.top // TILE_SIZE
        
        end_x = camera.rect.right // TILE_SIZE
        end_y = camera.rect.bottom // TILE_SIZE
        
        
        for y in range(start_y, min(end_y + 1, self.height)):
            for x in range(start_x, min(end_x + 1, self.width)):
                
                try:
                    image = self.tile[self.cell[x][y]]
                except:
                    log.error("tried to render non-existant tile ({}, {})".format(x, y))
                    image = self.tile[-1]
                
                screen.blit(image, camera.world_to_screen((x*TILE_SIZE, y* TILE_SIZE)))






