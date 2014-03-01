#!/usr/bin/python3

from objects.interactable import Interactable

import logging
log = logging.getLogger(__name__)

class Computer(Interactable):
    def __init__(self, image, location, collision_rect, area):
        super().__init__(image, location, collision_rect, area)

    def interact(self, interacter):
        log.info("{} interacted with computer".format(interacter))
        area = interacter.area
        area.display_message("Beep boop, this is a computer!")
