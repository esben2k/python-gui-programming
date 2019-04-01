from tkinter import *
import tkinter.messagebox


root = Tk()
root.withdraw()
#automatically hides main TK window

tkinter.messagebox.showinfo("Window Title","This is some information")
answer = tkinter.messagebox.askquestion("Question 1", "What is the question?")

if answer == "yes":
	print("Answer was 'yes'")

root.mainloop()