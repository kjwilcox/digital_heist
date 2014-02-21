#!/usr/bin/python3

import pygame


class InputDevice:
    def __init__(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.A = False
        self.B = False
        self.start = False
        self.select = False  
        

class KeyboardInput(InputDevice):
    def __init__(self):
        super().__init__()
        
    def update(self):
        keys = pygame.key.get_pressed()
        self.up = True if keys[pygame.K_UP] else False
        self.down = True if keys[pygame.K_DOWN] else False
        self.left = True if keys[pygame.K_LEFT] else False
        self.right = True if keys[pygame.K_RIGHT] else False
        self.A = True if (keys[pygame.K_SPACE] or keys[pygame.K_z]) else False
        self.B = True if (keys[pygame.K_LCTRL] or keys[pygame.K_x]) else False
        self.start = True if keys[pygame.K_RETURN] else False
        self.select = True if keys[pygame.K_BACKSPACE] else False
        
