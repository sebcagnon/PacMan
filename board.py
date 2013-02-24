"""Implementation of a board for console games like pacman
Author: Sebastien Cagnon
Date: 2013-Feb
"""
import tiles


class Board:
    def __init__(self, width=5, height=5, fromFile=None):
        """Creates empty 5x5 board by default. If fromFile is defined then load from file"""
        if fromFile:
            self.load(fromFile)
        else:
            self.create(width, height)

    def __str__(self):
        return '\n'.join([''.join([str(tile) for tile in line])
                          for line in self.map])

    def __getitem__(self, i):
        return self.map[i]

    def __setitem__(self, i, j=None):
        return self.map[i]

    def save(self, filePath):
        """Saves the current board to a file (usually .brd)"""
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
        """Loads a board from a .brd file"""
        f= open(filePath, 'r')
        self.map= []
        for line in f.readlines():
            print line
            self.map.append([
                tiles.shapes[line[i:i+2]] for i in range(0, len(line)-2, 2)])

    def create(self, width, height):
        """Creates a new board with only walls, with dimensions width and height"""
        w= tiles.Wall()
        t= tiles.Tile()
        self.map= [[w]*(width+2)]
        for _ in range(height):
            self.map.append([w]+[t]*width+[w])
        self.map.append([w]*(width+2))     


if __name__=='__main__':
    tileList= [tiles.Tile(), tiles.Wall(), tiles.Object()]
    assert [str(tile) for tile in tileList]==['  ', '++', '@@']
    board= Board(width=2,height=2)
    assert str(board)=='++++++++\n++    ++\n++    ++\n++++++++'
