import sys
import random
import math
import os
import getopt
import pygame
#from socket import *
from pygame.locals import *

def load_png(name):
    """Load PNG image and return image object"""
    fullname = os.path.dirname().join('res', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image, image.get_rect()

class Player(pygame.sprite.Sprite):
    """The main character"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ball.png') #TODO: retain direction
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector


