from tkinter import *

def get_val():
	print("Value = " + str(val.get()))
	label_1.config(text="Value = " +str(val.get()))

root = Tk()

val = DoubleVar()
scale = Scale(root, variable = val, orient = HORIZONTAL)
scale.pack()

button_1 = Button(root,text="Value of scale: ", command=get_val)
button_1.pack()

label_1 = Label(root)
label_1.pack()

root.mainloop()