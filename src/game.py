import os
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
WIDTH = 400
HEIGHT = 400

class App(object):
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.b= board.Board(
				  fromFile=os.path.join(RESSOURCES_FOLDER,'board1.brd'))
        self.player= self.b.getPlayers()[0]
        self.direction = False

    def keyPressed(self,event):
        if event.keysym == 'Escape':
            root.destroy()
        elif event.keysym in ['Right', 'Left', 'Up', 'Down']:
            self.direction = event.keysym

    def keyReleased(self,event):
        pass

    def task(self):
        if self.direction:
            self.player.setDirection(self.direction)
        self.b.moveAllCharacters()
        label.configure(text=str(self.b))
        tk.after(80,self.task)

pygame.init()


print "exiting"
