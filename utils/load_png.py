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
    if scale == 2:                              # if the game scale is 2x
        return pygame.transform.scale2x(image) # double the image size
    else:                                      # otherwise,
        width = pygame.Surface.get_width(image)
        height = pygame.Surface.get_height(image)
        scaledsize = (width * scale, height * scale) # just scale the image by game scale
        return pygame.transform.scale(image, scaledsize)
