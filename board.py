"""Implementation of a board for console games like pacman
Author: Sebastien Cagnon
Date: 2013-Feb
"""
import tiles
import character


class Board(object):
    def __init__(self, width=5, height=5, fromFile=None):
        """Creates empty 5x5 board by default. If fromFile is defined then load from file"""
        self.characters= []
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
        for n, line in enumerate(f.readlines()):
            newLine= []
            for i in range(0, len(line)-2, 2):
                currentObject= line[i:i+2]
                if currentObject in tiles.shapes.keys():
                    newLine.append(tiles.shapes[currentObject])
                elif currentObject in character.shapes.keys():
                    char= character.shapes[currentObject](self.newID())
                    self.characters.append(char)
                    newLine.append(char)
            self.map.append(newLine)
        #TODO check all lines have same lenght
        self.width= len(self.map[0])
        self.height= len(self.map)

    def create(self, width, height):
        """Creates a new board with only walls, with dimensions width and height"""
        w= tiles.Wall()
        t= tiles.Tile()
        self.map= [[w]*(width+2)]
        for _ in range(height):
            self.map.append([w]+[t]*width+[w])
        self.map.append([w]*(width+2))
        self.width= width
        self.height= height

    def newID(self):
        """Creates an ID for characters"""
        return len(self.characters)

    def availableDirections(self, pos):
        """Returns a dictionnary {direction:newPos} for available directions of ID"""
        i,j = pos
        available= {}
        checkSide= lambda x,y: (x in range(self.height)
                                and y in range(self.width)
                                and self.map[x][y].isFree())
        if checkSide(i-1,j):
            available['Up']= (i-1,j)
        if checkSide(i+1,j):
            available['Down']= (i+1,j)
        if checkSide(i,j-1):
            available['Left']= (i,j-1)
        if checkSide(i,j+1):
            available['Right']= (i,j+1)
        return available

    def getPosition(self, ID):
        """Returns the current position of ID"""
        for i,line in enumerate(self.map):
            for j,obj in enumerate(line):
                if isinstance(obj, character.Character) and obj.getID()==ID:
                    return (i,j)

    def move(self, ID):
        goal= self.characters[ID].getDirection()
        pos= self.getPosition(ID)
        available= self.availableDirections(pos)
        for direction in goal:
            if direction in available.keys():
                self.__displace(pos, available[direction])
                break

    def __displace(self, start, end, leaveBehind= tiles.Tile()):
        """move object at start to position end, leaves behind the leaveBehind tile"""
        i1,j1= start
        i2,j2= end
        temp= self.map[i1][j1]
        self.map[i1][j1]= leaveBehind
        self.map[i2][j2]= temp

    def moveAllCharacters(self):
        """Move all the characters on the map"""
        for i in range(len(self.characters)):
            self.move(i)

    def getPlayers(self):
        """Returns the list of playable characters"""
        return [obj for obj in self.characters
                if isinstance(obj, character.Player)]

if __name__=='__main__':
    tileList= [tiles.Tile(), tiles.Wall(), tiles.Object()]
    assert [str(tile) for tile in tileList]==['  ', '++', '@@']
    board= Board(width=2,height=2)
    assert str(board)=='++++++++\n++    ++\n++    ++\n++++++++'
    board1= Board(fromFile='ressources/board1.brd')
    print board1
    assert board1.getPosition(0)== (8,10)
    assert board1.availableDirections((8,10)) == {'Down':(9,10), 'Left':(8,9),
                                             'Right':(8,11)}
    assert len(board1.getPlayers()) == 1
    assert board1.getPlayers()[0].getID() == 3
    print "Tests passed"
