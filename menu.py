from tkinter import *

def copyfunction():
	statusbar.config(text="Copied")

def printsomething():
	print("Printing something")

root = Tk()
root.geometry("500x300")
#set dimensions of window

#Menu section ->
menubar = Menu(root)
"""Built-in menu from Tkinter"""

root.config(menu=menubar)
"""Configuring menubar"""

submenu = Menu(menubar, tearoff=0)
"""Init submenu"""
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New Project", command=printsomething)
submenu.add_command(label="New", command=printsomething)
submenu.add_separator()
submenu.add_command(label="Exit", command=root.destroy)

editmenu = Menu(menubar)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Redo", command=printsomething)

#Toolbar section ->
toolbar = Frame(root, bg="blue")
copy_button = Button(toolbar, text = "Copy", command=copyfunction)
print_button = Button(toolbar, text = "Print", command=printsomething)

copy_button.pack(side=LEFT, padx=2,pady=2)
print_button.pack(side=LEFT, padx=2,pady=2)
toolbar.pack(side=TOP,fill=X)

#Status bar section ->
statusbar = Label(root, text="Preparing the document", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()