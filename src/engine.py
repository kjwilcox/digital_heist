#!/usr/bin/python3


import exhibition
import map
import player

import pygame
import logging
log = logging.getLogger(__name__)

class Engine:
    
    def __init__(self):
        self.map = None
        self.player = player.Player()
        pygame.init()
        screen = pygame.display.set_mode((32*2*16,32*2*9))
        exhibition.optimize()
        
        
    def load_map(self, filename):
        self.map = map.Map(filename)
        
    
    def run(self):
        
        
        
        self.main_loop()
        pygame.quit()
    
    def main_loop(self):
        
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            if self.map:
                self.map.render()
                
            if self.player:
                self.player.render()
            
            pygame.display.flip()
            pygame.time.wait(50) # 20 fps


