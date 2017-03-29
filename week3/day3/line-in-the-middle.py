from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


horizontal_line = canvas.create_line(0, 150, 300, 150, fill='light sea green')

vertical_line = canvas.create_line(150, 0, 150, 300, fill='light sea green')

# draw a red horizontal line to the canvas' middle.
# draw a green vertical line to the canvas' middle.

root.mainloop()
