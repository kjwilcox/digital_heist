#!/usr/bin/python3

import logging
import os

import exhibition
import engine

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

DATA_DIR = ""
IMAGE_DIR = ""

try:
    data_location = open("../data_location.txt").read(2048).strip()
    if data_location:
        DATA_DIR = data_location
        log.info("Reading data files from " + data_location)
        IMAGE_DIR = os.path.join(data_location, "images")
except:
    pass
    



def main():
    exhibition.images(IMAGE_DIR)
    game = engine.Engine()
    game.load_map(os.path.join(DATA_DIR, "maps", "map1.txt"))
    game.run()
    





if __name__ == "__main__":
    main()

