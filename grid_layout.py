#grid_layout.py

from tkinter import *

root = Tk()

def checkstate():
	print("checkstate ran")
	if var.get() == 1:
		print("checkstate var is checked!")

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")

entry_1 = Entry(root)
entry_2 = Entry(root)


label_1.grid(row=0, column=0, sticky = W)
"""grid specifies where to place the element"""

label_2.grid(row=1, column=0, sticky = W)
"""sticky = alignment, E = east"""

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

var = IntVar()
c = Checkbutton(root, text="Keep me logged in",command=checkstate, variable=var)
"""command = function to run, no brackets needed"""
c.grid(columnspan=2)
"""columnspan=2 takes up to columns"""

root.mainloop()