import sys
import random
import math
#import getopt
import pygame
from os import path
#from socket import *
from pygame.locals import *

def load_png(name):
    """Load PNG image and return image object"""
    currentfolder = path.dirname(path.abspath(__file__))
    resfolder = path.join(path.dirname(currentfolder), 'res') # the resource folder is in the parent directory of this file's directory
    fullname = path.join(resfolder, name) # and the actual file path
    try:
        image = pygame.image.load(fullname) # load the file
        if image.get_alpha() is None:     # for a non-alpha PNG
            image = image.convert()       # optimise the image
        else:                             # but for an alpha PNG
            image = image.convert_alpha() # use an alpha-specific optimise
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    if scale = 2:                              # if the game scale is 2x
        return pygame.transform.scale2x(image) # double the image
    else:                                      # otherwise,
        scaledsize = (pygame.Surface.get_width(image) * scale, pygame.Surface.get_height(image) * scale) # just scale the image by game scale
        return image

class Player(pygame.sprite.Sprite):
    """The main character"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('') #TODO: retain direction
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption('Testing loading a tile')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((200, 200, 200))

image = load_png('grass1.png')
background.blit(image, image.get_rect())

screen.blit(background, (0,0))
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(1)

    screen.blit(background, (0,0))
    pygame.display.flip()



