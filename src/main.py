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

def nice_scale(surf):
    if scale == 2:
        return pygame.transform.scale2x(surf)
    else:
        width = pygame.Surface.get_width(surf)
        height = pygame.Surface.get_height(surf)
        scaledsize = (width * scale, height * scale)
        return pygame.transform.scale(surf, scaledsize)

class Player(pygame.sprite.Sprite):
    """The main character"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_png('player.png') #TODO: retain direction
        self.image = nice_scale(self.image)
        self.rect = self.image.get_rect()

    def move(self, direction):
        if direction == 'up':
            self.rect = self.rect.move(0, -1 * TILE_SIZE * scale)
        elif direction == 'left':
            self.rect = self.rect.move(-1 * TILE_SIZE * scale, 0)
        elif direction == 'down':
            self.rect = self.rect.move(0, TILE_SIZE * scale)
        else: # direction = 'right'
            self.rect = self.rect.move(TILE_SIZE * scale, 0)


pygame.init()
screen = pygame.display.set_mode((160 * scale, 144 * scale))
pygame.display.set_caption('Nompoke')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((200, 200, 200))

for y in xrange(0, 9):
    for x in xrange(0, 10):
        image = load_png('grass1.png')
        image = nice_scale(image)
        background.blit(image, image.get_rect().move(TILE_SIZE * scale * x, TILE_SIZE * scale * y))

player = Player()
csprites = pygame.sprite.RenderPlain(player)

screen.blit(background, (0,0))
pygame.display.flip()

while 1:
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit(1)
        elif e.type == KEYDOWN:
            if e.key == K_w:
                player.move('up')
            elif e.key == K_a:
                player.move('left')
            elif e.key == K_s:
                player.move('down')
            elif e.key == K_d:
                player.move('right')

    screen.blit(background, (0,0))
    screen.blit(background, player.rect, player.rect)
    csprites.draw(screen)
    pygame.display.flip()



