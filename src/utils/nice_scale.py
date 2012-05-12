import pygame

def nice_scale(scale, surf):
    if scale == 2:
        return pygame.transform.scale2x(surf)
    else:
        width = pygame.Surface.get_width(surf)
        height = pygame.Surface.get_height(surf)
        scaledsize = (width * scale, height * scale)
        return pygame.transform.scale(surf, scaledsize)
