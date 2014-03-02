#!/usr/bin/python3

from objects.interactable import Interactable

import level1

import exhibition
import logging
log = logging.getLogger(__name__)

class Level1Door(Interactable):
    def __init__(self, location, collision_rect, area):
        
        super().__init__(exhibition.images()["vwalldoor"], location, collision_rect, area)
        

    def interact(self, interacter):
        log.info("{} interacted with level1door".format(interacter))
        
        if self.enabled:
            area = interacter.area
            if area.level.mission_state == level1.Level1State.LookingForData:
                area.display_message("I can't leave yet, I haven't found the data.")
            else:
                area.display_message("Made it! Let's get this into my deck so I can analyze it.")
                area.level.mission_state = level1.Level1State.Complete
        
