#!/usr/bin/python3

import pygame

import map

class Engine:
    
    def __init__(self):
        self.map = None
        pygame.init()
        screen = pygame.display.set_mode((32*2*16,32*2*9))
        
        
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
            pygame.display.flip()
            pygame.time.wait(50) # 20 fps


