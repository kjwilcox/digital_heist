#!/usr/bin/python3

import logging
import os

import exhibition
import engine
import data

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def main():
    exhibition.images(os.path.join(data.DATA_DIR, "images"))
    game = engine.Engine()
    game.run()
    





if __name__ == "__main__":
    main()

