import tiles
import random

class Character(tiles.Tile):
    """A character is a movable object"""
    def __init__(self, ID):
        self.id= ID
        self.shape= "CC"
        self.direction= []

    def getDirection(self):
        """Returns the direction in which the character is going, there can be several"""
        return self.direction

    def getID(self):
        return ID

class Ghost(Character):
    """A very bad monster"""
    def __init__(self, ID):
        super(Ghost, self).__init__(ID)
        self.shape= "AA"
        self.direction= ['Up', 'Down', 'Left', 'Right']

    def chooseDirection(self):
        random.shuffle(self.direction)
        return self.direction


shapes = {"CC":Character,
          "AA":Ghost}

    
