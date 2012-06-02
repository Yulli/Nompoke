from os import path

import pygame
from pygame.locals import *

from get_resfolder import get_resfolder

def get_mus(name):
    """Return full path of background music ogg"""
    resfolder = get_resfolder()
    soundfolder = path.join(resfolder, 'sound') # folder containing sounds
    fullname = path.join(soundfolder, name + '.ogg') # actual file path
    return fullname
