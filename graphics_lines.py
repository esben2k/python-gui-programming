from tkinter import *

def delete_line():
	main_canvas.delete(line_1)


root = Tk()

delete_button = Button(root, text="Delete line_1", command=delete_line)
delete_button.pack()

main_canvas = Canvas(root, width=200, height=200)
main_canvas.pack()

green_box = main_canvas.create_rectangle(25,25,175,150, fill="pink")

line_1 = main_canvas.create_line(0,0,200,200, fill="green")
line_2 = main_canvas.create_line(50,0,200,200, fill="red")




root.mainloop()