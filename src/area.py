#!/usr/bin/python3

import physics
import camera

class Area:
    """ An area represents a discrete clice of gameplay data.
        It holds a map and a player (who moves around this map).
        It also owns a camera that centers on the player. """
        
        
    def __init__(self, _player, _map):
        """ Creates an area with the given player on the given map. """
        
        self.map = _map
        self.player = _player
        self.camera = camera.PlayerCenteredCamera(self.player, self.map)
    
    
    def process_input(self, _input):
        """ Passes input from the input device to the player. """
        
        self.player.process_input(_input)


    def update(self):
        """ Updates player, performs collision detection, and updates camera. """
        
        self.player.update()
        physics.PlayerWallPhysics.update(self.map, self.player)
        
        self.camera.update()


    def render(self):
        """ Renders the map and player using the camera's position. """
        
        self.map.render(self.camera)
        self.player.render(self.camera)


