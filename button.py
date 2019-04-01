#button.py
from tkinter import *

root = Tk()

def checkclicked():
	print("The button was clicked")

def checkevent(event):
	print("The button was clicked with button 1")

def callback(event):
    print ("clicked at", event.x, event.y)

button_1 = Button(root, text = "Click here", command=checkclicked)
button_1.pack()

button_2 = Button(root, text = "Click here")
button_2.bind("<Button-1>", checkevent)
button_2.pack()

frame = Frame(root, width=640, height=480)
frame.bind("<Button-1>", callback)
frame.pack()


root.mainloop()