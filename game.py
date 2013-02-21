import board
import Tkinter
from Tkconstants import *

b= board.Board(20,20)
tk=Tkinter.Tk(className="PacMan")
frame= Tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
label= Tkinter.Label(frame, text=str(b))
label.pack(fill=X, expand=1)
button= Tkinter.Button(frame, text="Exit", command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()

print "exiting"
