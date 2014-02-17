#!/usr/bin/python3

import logging
import exhibition
import os

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


IMAGE_DIR = r"D:\Dropbox\GitHub\digital_heist\images"

try:
    data_location = open("../data_location.txt").read(2048).strip()
    if data_location:
        log.info("Reading data files from " + data_location)
        IMAGE_DIR = os.path.join(data_location, "images")
except:
    pass
    



def main():
    print("test loading images")
    exhibition.images(IMAGE_DIR)
    





if __name__ == "__main__":
    main()

