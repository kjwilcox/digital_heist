#!/usr/bin/python3


import exhibition
import map
import player
import inputdevice
import data

from levels import level1

import os
import pygame
import logging
log = logging.getLogger(__name__)


class Engine:
    """ Main class responsible for running the game.
        Controls game setup and runs the main loop.
        Passes input to game and handles the event queue. """
    
    
    def __init__(self):
        """ Creates the display surface and loads the game assets. """
        
        pygame.init()
        log.info("Initializing display surface at {}x{}".format(
            data.SCREEN_RESOLUTION[0], data.SCREEN_RESOLUTION[1]))
        self.screen = pygame.display.set_mode(data.SCREEN_RESOLUTION)
        pygame.display.set_caption("digital heist")
        
        # load image resources
        exhibition.images(os.path.join(data.DATA_DIR, "images"))
        exhibition.optimize()
        
        self.level = level1.Level1()
        self.input = inputdevice.KeyboardInput()
        
    
    def run(self):
        """ Starts the game and runs the main game loop. """
        
        self.main_loop()
        pygame.quit()
    
    
    def main_loop(self):
        
        clock = pygame.time.Clock()
        
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
            complete = self.level.update()

            self.screen.fill((0, 0, 0))
            self.level.render()
            
            pygame.display.flip()
            ms = clock.tick(60)
            
            if complete:
                break


