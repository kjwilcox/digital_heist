#!/usr/bin/python3

import os
import logging
log = logging.getLogger(__name__)

DATA_DIR = os.path.join("..", "data")
log.info("Reading data files from: {}".format(DATA_DIR))

TILE_SIZE = 64
log.info("Tile size: {}".format(TILE_SIZE))

PLAYER_SIZE = 32
log.info("Player size: {}".format(PLAYER_SIZE))
