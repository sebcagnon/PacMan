import tiles
import random

class Character(tiles.Tile):
    """A character is a movable object"""
    def __init__(self, ID, color):
        self.__id= ID
        self.shape= color
        self.direction= []

    def getDirection(self):
        """Returns the direction in which the character is going, there can be several"""
        return self.direction

    def getID(self):
        return self.__id

class Ghost(Character):
    """A very bad monster"""
    def __init__(self, ID):
        super(Ghost, self).__init__(ID, 'red')
        self.direction= ['Up', 'Down', 'Left', 'Right']
        self.free= False
        self.char = "AA"

    def getDirection(self):
        random.shuffle(self.direction)
        return self.direction

class Player(Character):
    """A playable character (self.direction can be set)"""
    def __init__(self, ID):
        super(Player, self).__init__(ID, 'blue')
        self.direction= []
        self.free= True
        self.char = "MM"

    def setDirection(self, direction):
        if not direction in ['Up', 'Down', 'Left', 'Right']:
            return False
        self.direction= [direction]


shapes = {"CC":Character,
          "AA":Ghost,
          "MM":Player}

    
if __name__=="__main__":
    """testing"""
    myGhost= Ghost(1)
    assert str(myGhost)=="AA"
    assert myGhost.getID() == 1
    assert len(myGhost.getDirection()) == 4
    assert set(['Up', 'Down', 'Left', 'Right'])==set(myGhost.getDirection())
    print "tests passed"
