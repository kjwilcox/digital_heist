#!/usr/bin/python3

import logging
log = logging.getLogger(__name__)

class Map:
    
    def __init__(self, map_filename):
        self.tile = {}
        log.info("loading map from: " + map_filename)
        
        with open(map_filename, encoding="utf8") as f:
            dimensions = f.readline().strip().split()
            self.width, self.height = int(dimensions[0]), int(dimensions[1])
            log.debug("height: {}, width: {}".format(self.height, self.width))
            
            for i in range(self.width):
                self.tile[i] = {}
                

            for y, line in enumerate(f):
                log.debug("{}".format(line.strip()))
                
                for x, cell in enumerate(line.strip().split()):
                    self.tile[x][y] = int(cell)
                    
            print(self.tile)
                    
                    

    def render(self):
        pass
