#
# Copyright (c) 2008 Kyle J. Wilcox
# 
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#

"""
exhibition.py
A simple, general-purpose solution for graphics management.

Upon importing and activating the module, exhibition will
recursively traverse the specifed directory ("data\images"
is the default), and create a dictionary of the images. Any
file with a non-image extension will be ignored. Extensions
will be stripped, so it is not advisable to have two images
with the same name, but of different types.

The images will be in pygame.Surface format. They will be
in un-optimized formats until the appropriate function is
called. This must occur after the display surface is
created.

To initialize to module you must import is as such:

 import exhibition
 exhibition.images()
 # initialize screen...
 exhibition.optimize()

After this, you can either access the images with:
 exhibition.images()["foo"]
or you can use the return value of exhibition.images()
as a reference to the dict.
 img = exhibition.images()
 img["foo"]

"""

import pygame
import glob
import os
import logging

log = logging.getLogger(__name__)

if not pygame.image.get_extended():
    log.warning("Pygame will to be unable to load complex image formats.")

    
# the 'singleton' image dict
__images = None

# flag for whether __images has yet been optimized
__optimized = False

    
def images(directory=os.path.join("data","images")):
    """
    Returns a recursive dict of loaded images.
    Safe to call multiple times, it will always
    return the same dict.
    """
    
    global __images
    
    if not __images:
        __images = __load_images(directory)
        
    return __images


def optimize(alpha=True):
    """
    Optimizes the already-loaded dict for faster use.
    It is highly reccomended you use this functionality.
    """
    
    global __images
    
    if not __images:
        raise RuntimeError("No images loaded yet.")
    
    if __optimized:
        # we already did this, silently ignore the new request
        return
    
    if alpha:
        __optimize_alpha(__images)
    else:
        __optimize(__images)


def __load_images(directory):
    """ Auto-loads images in given directory and returns a dict. """
    try:
        return __get_dir_dict(directory)
    except StopIteration:
        raise RuntimeError("Could not load image directory.")


def __optimize(images):
    """
    Optimizes a dict of already loaded images (strips transparency).
    Only call after you have created your display surface.
    """

    for key in images:
        if type(images[key]) == dict:
            __optimize(images[key])
        else:
            images[key] = images[key].convert()


def __optimize_alpha(images):
    """
    Optimizes a dict of already loaded images (includes transparency).
    Only call after you have created your display surface.
    """

    for key in images:
        if type(images[key]) == dict:
            __optimize_alpha(images[key])
        else:
            images[key] = images[key].convert_alpha()


def __get_dir_dict(d):
    """
    Recursively traverses the filesystem and loads in images into
    a dict. It will throw a StopIterationError if it can't
    traverse for some reason.
    Should not be called directly.
    """
    listing = {}

    # just get the first entry, we don't want to scale the whole tree
    #  with os.walk, we need to do it manually
    gen = os.walk(d)
    
    try:
        parent, dirs, files = next(gen)
    except StopIteration:
        raise ValueError("Cannot traverse directory %s" % d)
    
    for f in files:
        ext = f.split('.')[-1]
        if ext.lower() in ('jpg', 'jpeg', 'png', 'gif', 'bmp'):
            image_path = os.path.join(parent, f)
            log.debug("loading: " + image_path)
            listing[''.join(f.split('.')[0:-1])] = pygame.image.load(image_path)
    for d in dirs:
        listing[d] = __get_dir_dict(os.path.join(parent, d))
 
    return listing

