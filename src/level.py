#!/usr/bin/python3

import physics

class Level:
    def __init__(self):
        pass
    
    def process_input(self, _input):
        self.playerA.process_input(_input)

    def update(self):
        self.playerA.update()
        
        physics.PlayerWallPhysics.update(self.mapA, self.playerA)
        
        self.cameraA.update()
        
    def render(self):
        self.mapA.render(self.cameraA)
        self.playerA.render(self.cameraA)
