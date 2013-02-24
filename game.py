import board
import Tkinter
import Image
from Tkconstants import *


class App(object):
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.b= board.Board(20,20)
        self.x= 10
        self.y= 10
        self.b[self.x][self.y]= board.Object()

    def keyPressed(self,event):
        if event.keysym == 'Escape':
            root.destroy()
        elif event.keysym == 'Right':
            self.right = True
        elif event.keysym == 'Left':
            self.left = True
        elif event.keysym == 'Up':
            self.up = True
        elif event.keysym == 'Down':
            self.down = True

    def keyReleased(self,event):
        if event.keysym == 'Right':
            self.right = False
        elif event.keysym == 'Left':
            self.left = False
        elif event.keysym == 'Up':
            self.up = False
        elif event.keysym == 'Down':
            self.down = False

    def task(self):
        if self.right:
            self.move(0,1)
        elif self.left:
            self.move(0,-1)
        elif self.up:
            self.move(-1,0)
        elif self.down:
            self.move(1,0)
        label.configure(text=str(self.b))
        tk.after(40,self.task)

    def move(self, dx,dy):
        self.b[self.x][self.y]= board.Tile()
        self.x+=dx
        self.y+=dy
        self.b[self.x][self.y]= board.Object()
        

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
tk.after(20, application.task)
tk.mainloop()

print "exiting"
