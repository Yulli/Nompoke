from os import path

def get_resfolder():
    """Return full path to res folder"""
    currentfolder = path.dirname(path.abspath(__file__))
    resfolder = path.join(path.dirname(path.dirname(currentfolder)), 'res') # the resource folder is in the parent directory of this file's directory
    return resfolder
