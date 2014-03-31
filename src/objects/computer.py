#!/usr/bin/python3

from objects.interactable import Interactable

import levels

import logging
log = logging.getLogger(__name__)


class Computer(Interactable):
    def __init__(self, image, location, collision_rect, area):
        super().__init__(image, location, collision_rect, area)

    def interact(self, interacter):
        log.info("{} interacted with computer".format(interacter))
        if self.enabled:
            area = interacter.area
            if area.level.mission_state == levels.level1.Level1State.LookingForData:
                area.display_message("I think this is the data I was looking for. It is! I had better get out of here while I still can.")
                area.level.mission_state = levels.level1.Level1State.Escape
            else:
                area.display_message("I already got the data, time to go!.")
