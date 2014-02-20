#!/usr/bin/python3

import os
import logging
log = logging.getLogger(__name__)

DATA_DIR = os.path.join("..", "data")
log.info("Reading data files from: {}".format(DATA_DIR))

