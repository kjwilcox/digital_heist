#!/usr/bin/python3

import physics

""" Contains 1 or more area. """
class Level:
    def __init__(self):
        self.areas = {}
        self.area = None
    
    def process_input(self, _input):
        self.area.player.process_input(_input)

    def update(self):
        self.area.update()
        
    def render(self):
        self.area.render()
