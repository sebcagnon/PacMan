import tiles
import random

class Character(tiles.Tile):
    """A character is a movable object"""
    def __init__(self, ID):
        self.__id= ID
        self.shape= "CC"
        self.direction= []

    def getDirection(self):
        """Returns the direction in which the character is going, there can be several"""
        return self.direction

    def getID(self):
        return self.__id

class Ghost(Character):
    """A very bad monster"""
    def __init__(self, ID):
        super(Ghost, self).__init__(ID)
        self.shape= "AA"
        self.direction= ['Up', 'Down', 'Left', 'Right']

    def getDirection(self):
        random.shuffle(self.direction)
        return self.direction


shapes = {"CC":Character,
          "AA":Ghost}

    
if __name__=="__main__":
    """testing"""
    myGhost= Ghost(1)
    assert str(myGhost)=="AA"
    assert myGhost.getID() == 1
    assert len(myGhost.getDirection()) == 4
    assert set(['Up', 'Down', 'Left', 'Right'])==set(myGhost.getDirection())
    print "tests passes"
