import board
import Tkinter
import Image
from Tkconstants import *

b= board.Board(20,20)
img= Image.new('1', (200,200))
for i in range(10, 150, 20):
	for j in range(10, 150, 20):
		for i2 in range(10):
			for j2 in range(10):
				img.putpixel((i+i2, j+j2), 200)

def myCallBack():
    b[10][10]=board.Object()
    label.configure(text=str(b))

tk=Tkinter.Tk(className="PacMan")
frame= Tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
bmp= Tkinter.BitmapImage(name="bmp", data= img.tobitmap())
##label= Tkinter.Label(frame, text=str(b), font='TkFixedFont')
##label.bind(sequence='<Alt-A>', func=myCallBack)
##label.pack(fill=X, expand=1)
c = Tkinter.Canvas(tk, width=200, height=200); c.pack()
c.create_image(0, 0, image = bmp, anchor=Tkinter.NW)
button= Tkinter.Button(frame, text="Exit", command=myCallBack)
button.pack(side=BOTTOM)
tk.mainloop()

print "exiting"
