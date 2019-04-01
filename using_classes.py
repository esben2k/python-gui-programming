from tkinter import *

class Learninggui:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		self.printbutton = (Button(master, text="Printing Message", command=self.printmessage))
		self.quitbutton = (Button(master, text="Quit", command=master.quit))

		self.printbutton.pack(side=LEFT)
		self.quitbutton.pack(side=LEFT)

	def printmessage(self):
		print("printmessage ran")

	



root = Tk()
Learninggui(root)
root.mainloop()