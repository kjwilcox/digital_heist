#!/usr/bin/python3

import level
import data

import exhibition
import player
import map
import area
import objects.computer
import objects.lvl1door
from data import TILE_SIZE

import pygame
import os

import logging
log = logging.getLogger(__name__)


class Level1(level.Level):
    
    def __init__(self):
        super().__init__()
        
        p = player.Player((96.0,96.0))
        m = map.Map(os.path.join(data.DATA_DIR, "maps", "map1.txt"))
        area1 = area.Area(p, m, self)
        
        computer1 = objects.computer.Computer(
            exhibition.images()["computer"],
            pygame.Rect(map.Map.tile_to_world_coords((3,3)), (TILE_SIZE/2, TILE_SIZE/2)),
            pygame.Rect(map.Map.tile_to_world_coords((3,3)), (TILE_SIZE/2, TILE_SIZE/2)),
            area1
        )
        
        exitdoor = objects.lvl1door.Level1Door(
            pygame.Rect(map.Map.tile_to_world_coords((0,1)), (TILE_SIZE, TILE_SIZE)),
            pygame.Rect(map.Map.tile_to_world_coords((0,1)), (TILE_SIZE, TILE_SIZE)),
            area1
        )
        
        area1.interactables["comp1"] = computer1
        area1.interactables["exitdoor"] = exitdoor
        
        
        self.areas[1] = area1
        self.area = self.areas[1]
        
        self.mission_state = Level1State.LookingForData
        
        
    def update(self):
        if self.mission_state == Level1State.Complete:
            log.info("mission complete")
            self.complete = True
            
        return super().update()
        

class Level1State:
    LookingForData, Escape, Complete = range(3)
