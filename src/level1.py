#!/usr/bin/python3

import level
import player
import map
import area
import data
import camera

import os

class Level1(level.Level):
    def __init__(self):
        super().__init__()
        
        
        p = player.Player((96.0,96.0))
        m = map.Map(os.path.join(data.DATA_DIR, "maps", "map1.txt"))
        c = camera.Camera(p, m)
        self.areas[1] = area.Area(p, m, c)
        self.area = self.areas[1]

