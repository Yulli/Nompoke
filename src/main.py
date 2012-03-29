import sys
import random
import math
import os
#import getopt
import pygame
#from socket import *
from pygame.locals import *

def load_png(name):
    """Load PNG image and return image object"""
    resfolder = os.path.join(os.path.dirname(os.getcwd()), 'res')
    fullname = os.path.join(resfolder, name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
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
screen = pygame.display.set_mode((200, 200))
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



