#!/usr/bin/python3


import exhibition
import map
import player
import inputdevice

import pygame
import logging
log = logging.getLogger(__name__)

class Engine:
    
    def __init__(self):
        self.map = None
        self.player = player.Player()
        self.input = inputdevice.KeyboardInput()
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
            
            # game update
            self.input.update()
            self.player.process_input(self.input)
            
            self.player.update()
            
            
                
            if self.map:
                self.map.render()
                
            if self.player:
                self.player.render()
            
            pygame.display.flip()
            pygame.time.wait(16) # 20 fps


