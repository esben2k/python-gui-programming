from tkinter import *

root = Tk()

def leftclick(event):
	print("Left")
def rightclick(event):
	print("Right")
def middleclick(event):
	print("Middle")


frame = Frame(root, width=200, height=300)
frame.bind("<Button-1>", leftclick)
frame.bind("<Button-3>", rightclick)
frame.bind("<Button-2>", middleclick)
frame.pack()

root.mainloop()