import sys
import math
import time

import pygame
from pygame.locals import *

from utils.load_map import load_map
from utils.load_png import load_png
from utils.load_snd import load_snd
from utils.nice_scale import nice_scale

DEFAULT_SCALE = 4
TILE_SIZE = 16
FPS = 60

scale = DEFAULT_SCALE

class Player(pygame.sprite.Sprite):
    """The main character"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_png('playerdown.png') #TODO: retain direction
        self.image = nice_scale(scale, self.image)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(0, -4 * scale)
        self.movedirsh = []
        self.movedirsv = []
        self.lastmove = time.time()

    def update(self):
        if (self.movedirsh.__len__() != 0 or \
           self.movedirsv.__len__() != 0) and \
           time.time() - self.lastmove >= 0.2:
            if self.movedirsv.__len__() != 0:
                self.move(self.movedirsv[0])
            elif self.movedirsh.__len__() != 0:
                self.move(self.movedirsh[0])
            self.lastmove = time.time()

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
clock = pygame.time.Clock()
screen = pygame.display.set_mode((160 * scale, 144 * scale))
pygame.display.set_caption('Nompoke')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

#for y in xrange(0, 9):
#    for x in xrange(0, 10):
#        image = load_png('grass1.png')
#        image = nice_scale(image)
#        background.blit(image, image.get_rect().move(TILE_SIZE * scale * x, TILE_SIZE * scale * y))

world = load_map('room', screen)
world = nice_scale(scale, world)
bgmusic = load_snd('pallet.ogg')

player = Player()
csprites = pygame.sprite.RenderPlain(player)

screen.blit(background, (0,0))
screen.blit(world, (0,0))
pygame.display.flip()
bgmusic.play(-1) # play bgmusic forever

while 1:
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit(1)
        elif e.type == KEYDOWN:
            if e.key == K_w:
                player.movedirsv.append('up')
            elif e.key == K_a:
                player.movedirsh.append('left')
            elif e.key == K_s:
                player.movedirsv.append('down')
            elif e.key == K_d:
                player.movedirsh.append('right')
        elif e.type == KEYUP:
            if e.key == K_w:
                player.movedirsv.remove('up')
            elif e.key == K_a:
                player.movedirsh.remove('left')
            elif e.key == K_s:
                player.movedirsv.remove('down')
            elif e.key == K_d:
                player.movedirsh.remove('right')

    screen.blit(background, (0,0))
    screen.blit(background, player.rect, player.rect)
    screen.blit(world, (0,0))
    csprites.update()
    csprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
