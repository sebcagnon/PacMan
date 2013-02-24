"""Implementation of a board for console games like pacman
Author: Sebastien Cagnon
Date: 2013-Feb
"""
from tiles import Tile, Wall, Object, Ghost


class Board:
    def __init__(self, width=5, height=5, fromFile=None):
        self.shapes= {str(Tile()):Tile(),
                      str(Wall()):Wall(),
                      str(Object()):Object(),
                      str(Ghost()):Ghost()}
        if fromFile:
            self.load(fromFile)
        else:
            self.map= [[Wall()]*(width+2)]
            for _ in range(height):
                self.map.append([Wall()]+[Tile()]*width+[Wall()])
            self.map.append([Wall()]*(width+2))

    def __str__(self):
        return '\n'.join([''.join([str(tile) for tile in line])
                          for line in self.map])

    def __getitem__(self, i):
        return self.map[i]

    def __setitem__(self, i, j=None):
        return self.map[i]

    def save(self, filePath):
        count=0
        try:
            open(filePath, 'r')
            print "The file already exist: " + filePath
            while count<3:
                ans=raw_input("Do you want to want to rewrite the file (Y/n)? ")
                if ans=='Y':
                    break
                elif ans=='n':
                    return False
                else:
                    print "Invalid input. Type 'Y' or 'n' without quotes"
                count+=1
        except IOError:
            pass
        if count==3:
            return False
        open(filePath, 'w').write(str(self))
        return True

    def load(self, filePath):
        f= open(filePath, 'r')
        self.map= []
        for line in f.readlines():
            print line
            self.map.append([
                self.shapes[line[i:i+2]] for i in range(0, len(line)-2, 2)])
                


if __name__=='__main__':
    tiles= [Tile(), Wall(), Object()]
    assert [str(tile) for tile in tiles]==['  ', '++', '@@']
    board= Board(width=2,height=2)
    assert str(board)=='++++++++\n++    ++\n++    ++\n++++++++'
