#!/usr/bin/python3

import physics

class Area:
    def __init__(self, _player, _map, _camera):
        self.map = _map
        self.player = _player
        self.camera = _camera
    
    def process_input(self, _input):
        self.player.process_input(_input)

    def update(self):
        self.player.update()
        
        physics.PlayerWallPhysics.update(self.map, self.player)
        
        self.camera.update()
        
    def render(self):
        self.map.render(self.camera)
        self.player.render(self.camera)


