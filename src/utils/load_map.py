from os import path
from load_png import load_png
import pygame
from pygame.locals import *

def load_map(name, screen):
    """Load map and return image object"""
    currentfolder = path.dirname(path.abspath(__file__))
    mapfolder = path.join(path.dirname(path.dirname(currentfolder)), 'maps')
    fullname = path.join(mapfolder, name)

    mapsurf = pygame.Surface(screen.get_size())
    mapfile = open(fullname, 'r')
    ycount = 0
    for row in mapfile:
        xcount = 0
        row = row[0:-1]
        tiles = row.split(' ')
        for tile in tiles:
            tileimg = load_png(tile)
            mapsurf.blit(tileimg, (16 * xcount, 16 * ycount))
            xcount += 1
        ycount += 1
    return mapsurf
