#!/usr/bin/python3


import exhibition
import map
import player
import inputdevice

import level1

import pygame
import logging
log = logging.getLogger(__name__)

class Engine:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((32*2*16,32*2*9))
        exhibition.optimize()
        
        self.level = level1.Level1()
        self.input = inputdevice.KeyboardInput()
        
    
    def run(self):
        self.main_loop()
        pygame.quit()
    
    def main_loop(self):
        
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        return
            
            # game update
            self.input.update()
            
            self.level.process_input(self.input)
            self.level.update()
            
            self.level.render()
            
            pygame.display.flip()
            pygame.time.wait(16) # 20 fps


