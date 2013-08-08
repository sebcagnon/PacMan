"""Implementation of a board for console games like pacman
Author: Sebastien Cagnon
Date: 2013-Feb
"""


class Tile(object):
    """An empty tile"""
    def __init__(self, color):
        self.shape= color
        self.free= True
        self.char = "  "

    def __str__(self):
        return str(self.char)

    def isFree(self):
        """Returns True if you can walk on it, False otherwise"""
        return self.free
    

class Wall(Tile):
    """A tile you can't go through"""
    def __init__(self):
        self.shape= 'white'
        self.free= False
        self.char = "++"

class Object(Tile):
    """An eatable object"""
    def __init__(self):
        self.shape= 'green'
        self.free = True
        self.char = "OO"

shapes= {str(Tile('black')):Tile('black'),
         str(Wall()):Wall(),
         str(Object()):Object()}
