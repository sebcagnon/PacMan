"""Implementation of a board for console games like pacman
Author: Sebastien Cagnon
Date: 2013-Feb-21
"""

class Tile:
    """An empty tile"""
    def __init__(self):
        self.shape= " "

    def display(self):
        return str(self.shape)

class Wall(Tile):
    """A tile you can't go through"""
    def __init__(self):
        self.shape= chr(1)

class Object(Tile):
    def __init__(self):
        self.shape= chr(64)

class Board:
    def __init__(self):
        pass

    def display(self):
        pass


if __name__=='__main__':
    tiles= [Tile(), Wall(), Object()]
    assert [tile.display() for tile in tiles]==[' ', '\x01', '@']
