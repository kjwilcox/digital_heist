#!/usr/bin/python3

import level
import player
import map
import data
import camera

import os

class Level1(level.Level):
    def __init__(self):
        self.playerA = player.Player((64.0,64.0))
        self.mapA = map.Map(os.path.join(data.DATA_DIR, "maps", "map1.txt"))
        self.cameraA = camera.Camera(self.playerA, self.mapA)
                             
                                

