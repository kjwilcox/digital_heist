#!/usr/bin/python3

import logging
import os

import exhibition
import engine

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

DATA_DIR = os.path.join("..", "data")
log.info("Reading data files from: {}".format(DATA_DIR))



def main():
    exhibition.images(os.path.join(DATA_DIR, "images"))
    game = engine.Engine()
    game.load_map(os.path.join(DATA_DIR, "maps", "map1.txt"))
    game.run()
    





if __name__ == "__main__":
    main()

