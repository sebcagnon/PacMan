"""Implementation of a board for console games like pacman
Author: Sebastien Cagnon
Date: 2013-Feb-21
"""

class Tile:
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
    def __init__(self):
        self.shape= chr(64)*2

class Board:
    def __init__(self, width=5, height=5, fromFile=None):
        if fromFile:
            self.map= eval(open(fromFile, 'r').read())
        else:
            self.map= [[Wall()]*(width+2)]
            for _ in range(height):
                self.map.append([Wall()]+[Tile()]*width+[Wall()])
            self.map.append([Wall()]*(width+2))

    def __str__(self):
        return '\n'.join([''.join([str(tile) for tile in line])
                          for line in self.map])

    def __getitem__(self, n):
        return self.map[n]


if __name__=='__main__':
    tiles= [Tile(), Wall(), Object()]
    assert [str(tile) for tile in tiles]==['  ', '++', '@@']
    board= Board(width=2,height=2)
    assert str(board)=='++++++++\n++    ++\n++    ++\n++++++++'