#!/usr/bin/python3

import level
import data

import player
import map
import area

import os


class Level1(level.Level):
    
    def __init__(self):
        super().__init__()
        
        p = player.Player((96.0,96.0))
        m = map.Map(os.path.join(data.DATA_DIR, "maps", "map1.txt"))
        self.areas[1] = area.Area(p, m)
        self.area = self.areas[1]

