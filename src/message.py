#!/usr/bin/python3

import pygame
import textrect
import data

import logging
log = logging.getLogger(__name__)



class MessageBox:
    """
    A message box appears on the screen, displays text, and pauses the game until it is dismissed.
    """
    
    
    def __init__(self, msg, area, callback=None):
        """ Creates a message box with the given message for the given area. """
        
        self.creation_time = pygame.time.get_ticks()
        self.message = msg
        self.area = area
        self.callback = callback
        self.font = pygame.font.Font(None, 36)
        self.state = MessageBoxState.WaitingForInitialRelease
        
        screen = pygame.display.get_surface().get_rect()
        message_rect = pygame.Rect(0,0,1,1)
        message_rect.width = screen.width - (screen.width * 0.2)
        message_rect.height = screen.height * 0.2
        message_rect.midbottom = screen.midbottom
        message_rect.y -= screen.height * 0.1
        self.rect = message_rect
        
        self.surf = textrect.render_textrect(self.message, self.font, self.rect, (0,0,0), (255,255,255))
        
        
    def render(self):
        """ Renders the box to the screen. """
        
        screen = pygame.display.get_surface()
        screen.blit(self.surf, self.rect)
        
    
    def process_input(self, i):
        """ Handles input for dismissing the screen. """
        
        current_time = pygame.time.get_ticks()
        delta_t = current_time - self.creation_time
        
        if self.state == MessageBoxState.WaitingForInitialRelease and not i.A:
            self.state = MessageBoxState.WaitingForDismissal
            return
        
        if self.state == MessageBoxState.WaitingForDismissal and delta_t > data.MESSAGE_BOX_DELAY and i.A:
            self.state = MessageBoxState.WaitingForFinalRelease
            return
            
        if self.state == MessageBoxState.WaitingForFinalRelease and not i.A:
            self.area.remove_message()
            return
        

        
class MessageBoxState:
    """ Message box states. Refers to their logic for waiting on button presses. """
    WaitingForInitialRelease, WaitingForDismissal, WaitingForFinalRelease = range(3)
