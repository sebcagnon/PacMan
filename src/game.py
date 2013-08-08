import os
import sys
import board
import tiles
import pygame
from pygame.locals import *

RESSOURCES_FOLDER = "../ressources"

colors = { 'white': [255,255,255],
           'red':   [255,  0,  0],
           'green': [  0,255,  0],
           'blue':  [  0,  0,255],
           'black': [  0,  0,  0] }
           
FPS = 30
WIDTH = 800
HEIGHT = 800

def terminate():
    pygame.quit()
    print "exiting"
    sys.exit()

class App(object):
    def __init__(self, display):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.b= board.Board(
				  fromFile=os.path.join(RESSOURCES_FOLDER,'board1.brd'))
        self.player= self.b.getPlayers()[0]
        self.direction = False
        self.directionDict = {K_w:'Up', K_a:'Left', K_s:'Down', K_d:'Right'}
        self.tileW = WIDTH/self.b.width
        self.tileH = HEIGHT/self.b.height
        self.display = display

    def checkForDirection(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in self.directionDict.keys():
                    self.direction = self.directionDict[event.key]

    def task(self):
        if not self.checkForQuit():
            return False
        self.checkForDirection()
        if self.direction:
            self.player.setDirection(self.direction)
        self.b.moveAllCharacters()
        self.draw()
        return True
    
    def checkForQuit(self):
        for event in pygame.event.get(QUIT):
            return False
        for event in pygame.event.get(KEYUP):
            if event.key == K_ESCAPE:
                return False
            pygame.event.post(event)
        return True
        
    def draw(self):
        self.display.fill(colors['black'])
        for i, row in enumerate(self.b.map):
            for j, tile in enumerate(row):
                pygame.draw.rect(self.display, colors[tile.shape], 
                    (j*self.tileW, i*self.tileH, self.tileW, self.tileH))

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('PacMan')
    
    app = App(display)
    
    isRunning = True
    while isRunning:
        isRunning = app.task()
        pygame.display.update()
        clock.tick(FPS)
    
    terminate()

if __name__=='__main__':
    try:
        main()
    except:
        pygame.quit()
        raise
