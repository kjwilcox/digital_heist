#!/usr/bin/python3

import pygame


class InputDevice:
    """ A generic input device with a D-Pad and 4 buttons. Abstract base class."""

    def __init__(self):
        """ Abstract input device initializer. """
        
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.a_button = False
        self.b_button = False
        self.start = False
        self.select = False  
        

class KeyboardInput(InputDevice):
    """ A class for controlling the game with the keyboard. """

    def __init__(self):
        super().__init__()

    def update(self):
        """ Reads the state of the keyboard and updates the virtual controller accordingly. """
        
        keys = pygame.key.get_pressed()
        self.up = True if keys[pygame.K_UP] else False
        self.down = True if keys[pygame.K_DOWN] else False
        self.left = True if keys[pygame.K_LEFT] else False
        self.right = True if keys[pygame.K_RIGHT] else False
        self.a_button = True if (keys[pygame.K_SPACE] or keys[pygame.K_z]) else False
        self.b_button = True if (keys[pygame.K_LCTRL] or keys[pygame.K_x]) else False
        self.start = True if keys[pygame.K_RETURN] else False
        self.select = True if keys[pygame.K_BACKSPACE] else False

