#!/usr/bin/python3

import physics
import camera
import message

import logging
log = logging.getLogger(__name__)


class Area:
    """ An area represents a discrete slice of gameplay data.
        It holds a map and a player (who moves around this map).
        It also owns a camera that centers on the player. """

    def __init__(self, _player, _map, _level):
        """ Creates an area with the given player on the given map. """
        
        self.map = _map
        self.map.area = self
        self.player = _player
        self.player.area = self
        self.level = _level
        self.camera = camera.PlayerCenteredCamera(self.player, self.map)
        self.interactables = {}
        self.state = AreaState.Gameplay
        self.guards = {}
        self.message = None

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
            
            for guard in self.guards.values():
                guard.update()
            
            # guard physics
            
            self.camera.update()
        elif self.state == AreaState.Message:
            pass

    def render(self):
        """ Renders the map and player using the camera's position. """
        
        self.map.render(self.camera)
        
        for k, i in self.interactables.items():
            i.render(self.camera)
        
        for guard in self.guards.values():
            guard.render(self.camera)
        
        self.player.render(self.camera)

        if self.state == AreaState.Message:
            self.message.render()

    def display_message(self, msg, callback=None):
        """ Pops up a message window and pauses the game. """
        
        log.debug("Creating message")
        
        self.state = AreaState.Message
        self.message = message.MessageBox(msg, self, callback)

    def remove_message(self):
        """ Removes the message windows and resumes the game. """
        
        log.debug("removing message")
        callback = self.message.callback
        self.message = None
        self.state = AreaState.Gameplay
        if callback:
            callback()
        

class AreaState:
    """ The states that an area can be in. """
    Gameplay, Paused, Suspended, Message = range(4)
