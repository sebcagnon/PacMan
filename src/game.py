import board
import tiles
import Tkinter
import os
from Tkconstants import *

RESSOURCES_FOLDER = "../ressources"

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

        

application= App()
tk=Tkinter.Tk(className="PacMan")
frame= Tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)

label= Tkinter.Label(frame, text=str(application.b), font='TkFixedFont')
label.bind(sequence='<Key>', func=application.keyPressed)
label.bind(sequence='<KeyRelease>', func=application.keyReleased)
label.pack(fill=X, expand=1)

button= Tkinter.Button(frame, text="Exit", command=tk.destroy)
button.pack(side=BOTTOM)

label.focus_set()
tk.after(40, application.task)
tk.mainloop()

print "exiting"
