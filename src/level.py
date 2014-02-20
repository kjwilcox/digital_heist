#!/usr/bin/python3


class Level:
    def __init__(self):
        pass
    
    def process_input(self, _input):
        self.playerA.process_input(_input)

    def update(self):
        self.playerA.update()
        
    def render(self):
        self.mapA.render(self.cameraA)
        self.playerA.render(self.cameraA)
