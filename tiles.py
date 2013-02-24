"""Implementation of a board for console games like pacman
Author: Sebastien Cagnon
Date: 2013-Feb
"""


class Tile(object):
    """An empty tile"""
    def __init__(self):
        self.shape= "  "

    def __str__(self):
        return str(self.shape)
    

class Wall(Tile):
    """A tile you can't go through"""
    def __init__(self):
        self.shape= '++'

class Object(Tile):
    """An eatable object"""
    def __init__(self):
        self.shape= chr(64)*2

shapes= {str(Tile()):Tile(),
         str(Wall()):Wall(),
         str(Object()):Object()}
