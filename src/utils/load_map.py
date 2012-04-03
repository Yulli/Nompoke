from os import path
from load_png import load_png
import pygame
from pygame.locals import *

def load_map(name):
    """Load map and return image object"""
    currentfolder = path.dirname(path.abspath(__file__))
    mapfolder = path.join(path.dirname(path.dirname(currentfolder)), 'maps')
    fullname = path.join(mapfolder, name)

    mapsurf = pygame.Surface
    mapfile = open(fullname, 'r')
    ycount = 0
    for row in mapfile:
        xcount = 0
        row = row[0:-1]
        tiles = row.split(' ')
        for tile in tiles:
            tileimg = load_png(tile.__add__('.png'))
            mapsurf.blit(tileimg, (16 * xcount, 16 * ycount))
            xcount += 1
        ycount += 1
    return mapsurf
