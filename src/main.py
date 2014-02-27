#!/usr/bin/python3

import logging

import engine


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def main():
    game = engine.Engine()
    game.run()
    

if __name__ == "__main__":
    main()

