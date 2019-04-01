#main.py

from tkinter import *

root = Tk()
""" Constructor, creates tk window """


one = Label(root, text="One", fg="white", bg="blue")
one.pack(fill=BOTH, expand=True)
"""fill color in both axis and expand"""

two = Label(root, text="Two", fg="black", bg="yellow")
two.pack(fill=X)
"""fill color on the X-axis"""


three = Label(root, text="Three", fg="green", bg="white")
three.pack(side=LEFT,fill=Y)
"""fill color on the Y-axis"""


root.title("This is the window title")

myLabel = Label(root, text="This is the window text")

#root.iconbitmap('images\\black_cat.ico')
"""window icon, top left"""

myLabel.pack()
"""Init labels, pack window - reduces size """

"""Display 3 buttons top frame, 1 button bottom frame """
topFrame = Frame(root)
topFrame.pack(side=TOP)
"""pack is used to apply item to window"""

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button1", fg="red")
button2 = Button(topFrame, text="Button2", fg="green")
button3 = Button(topFrame, text="Button3", fg="blue")
button4 = Button(bottomFrame, text="Button4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()


root.mainloop()

