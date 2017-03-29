from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

top_line = canvas.create_line(50, 50, 100, 50, fill='light sea green')
right_line = canvas.create_line(100, 50, 100, 100, fill='yellow')
bottom_line = canvas.create_line(100, 100, 50, 100, fill='red')
left_line = canvas.create_line(50, 100, 50, 50, fill='blue')


# draw a box that has different colored lines on each edge.

root.mainloop()
