from tkinter import *

root = Tk()

image_1 = PhotoImage(file="images\\alien5.png")
label_1 = Label(root, image=image_1)
label_1.pack()

root.mainloop()