import sys
import random
import math
import pygame
#from socket import *
from pygame.locals import *

from utils.load_png import load_png

DEFAULT_SCALE = 4
TILE_SIZE = 16

scale = DEFAULT_SCALE

class Player(pygame.sprite.Sprite):
    """The main character"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_png('player.png') #TODO: retain direction
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

pygame.init()
screen = pygame.display.set_mode((160 * scale, 144 * scale))
pygame.display.set_caption('Nompoke')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((200, 200, 200))

for y in xrange(0, 9):
    for x in xrange(0, 10):
        image = load_png('grass1.png')
        if scale == 2:
            image = pygame.transform.scale2x(image)
        else:
            width = pygame.Surface.get_width(image)
            height = pygame.Surface.get_width(image)
            scaledsize = (width * scale, height * scale)
            image = pygame.transform.scale(image, scaledsize)
        background.blit(image, image.get_rect().move(TILE_SIZE * scale * x, TILE_SIZE * scale * y))

screen.blit(background, (0,0))
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(1)

    screen.blit(background, (0,0))
    pygame.display.flip()



