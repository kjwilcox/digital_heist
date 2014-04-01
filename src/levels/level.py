#!/usr/bin/python3


class Level:
    """
    A Level is an abstract base class, which must be overridden by an actual level.
    A Level is a container for one or more areas in a mission.
    A level should always have an active area set. This active area
    will receive update calls, input, and rendering calls.
    """

    def __init__(self):
        """ Abstract constructor for level with no areas. """
        self.areas = {}
        self.area = None
        self.complete = False

    def process_input(self, _input):
        """ Passes input to the current area. """
        self.area.process_input(_input)

    def update(self):
        """ Passes update call to current area. Returns whether or not the level is complete. """
        self.area.update()
        return self.complete

    def render(self):
        """ Passes render call to current area. """
        self.area.render()
