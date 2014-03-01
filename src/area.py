#!/usr/bin/python3

import physics
import camera

import message
import pygame

class Area:
    """ An area represents a discrete slice of gameplay data.
        It holds a map and a player (who moves around this map).
        It also owns a camera that centers on the player. """
        
        
    def __init__(self, _player, _map):
        """ Creates an area with the given player on the given map. """
        
        self.map = _map
        self.map.area = self
        self.player = _player
        self.player.area = self
        self.camera = camera.PlayerCenteredCamera(self.player, self.map)
        self.interactables = {}
        self.state = AreaState.Gameplay
    
    
    def process_input(self, _input):
        """ Passes input from the input device to the player. """
        
        if self.state == AreaState.Gameplay:
            self.player.process_input(_input)
        elif self.state == AreaState.Message:
            self.message.process_input(_input)

    def update(self):
        """ Updates player, performs collision detection, and updates camera. """
        if self.state == AreaState.Gameplay:
            self.player.update()
            physics.PlayerWallPhysics.update(self.map, self.player)
            
            self.camera.update()
        elif self.state == AreaState.Message:
            pass

    def render(self):
        """ Renders the map and player using the camera's position. """
        
        self.map.render(self.camera)
        
        for k, i in self.interactables.items():
            i.render(self.camera)
            
        self.player.render(self.camera)
        
        if self.state == AreaState.Message:
            self.message.render()
        
        
    def display_message(self, msg):
        self.state = AreaState.Message
        self.message = message.MessageBox(msg, self)
        
    
    def remove_message(self):
        self.message = None
        self.state = AreaState.Gameplay
        
        

class AreaState:
    Gameplay, Paused, Suspended, Message = range(4)