from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a green 10x10 square to the center of the canvas.

green_box = canvas.create_rectangle(145, 145, 155, 155, fill = 'green')


root.mainloop()
