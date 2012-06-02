from os import path
import pygame
from pygame.locals import *

def load_snd(name):
    """Load audio file and return Sound object"""
    currentfolder = path.dirname(path.abspath(__file__))
    resfolder = path.join(path.dirname(path.dirname(currentfolder)), 'res') # the resource folder is in the parent directory of this file's directory
    soundfolder = path.join(resfolder, 'sound') # folder containing sounds
    fullname = path.join(soundfolder, name) # and the actual file path
    try:
        return pygame.mixer.Sound(fullname) # load the file and put it into a Sound object
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message
