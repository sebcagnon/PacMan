import board
import Tkinter
import Image
from Tkconstants import *

b= board.Board(20,20)
b[10][10]=board.Object()
x=10
y=10
img= Image.new('1', (200,200))
for i in range(10, 150, 20):
	for j in range(10, 150, 20):
		for i2 in range(10):
			for j2 in range(10):
				img.putpixel((i+i2, j+j2), 200)

class App(object):
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False

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
        label.configure(text=str(b))
        tk.after(40,self.task)

    def move(self, dx,dy):
        global x,y
        b[x][y]= board.Tile()
        x+=dx
        y+=dy
        b[x][y]= board.Object()
        

application= App()
tk=Tkinter.Tk(className="PacMan")
frame= Tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
bmp= Tkinter.BitmapImage(name="bmp", data= img.tobitmap())
label= Tkinter.Label(frame, text=str(b), font='TkFixedFont')
label.bind(sequence='<Key>', func=application.keyPressed)
label.bind(sequence='<KeyRelease>', func=application.keyReleased)
label.pack(fill=X, expand=1)
#c = Tkinter.Canvas(tk, width=200, height=200); c.pack()
#c.create_image(0, 0, image = bmp, anchor=Tkinter.NW)
button= Tkinter.Button(frame, text="Exit", command=tk.destroy)
button.pack(side=BOTTOM)
label.focus_set()
tk.after(20, application.task)
tk.mainloop()

print "exiting"
