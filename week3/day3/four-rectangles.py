from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.
green_box = canvas.create_rectangle(0, 0, 50, 50, fill = 'green')
red_box = canvas.create_rectangle(50, 50, 150, 150, fill = 'red')
yellow_box = canvas.create_rectangle(200, 0, 300, 300, fill = 'yellow')
blue_box = canvas.create_rectangle(150,150, 300, 300, fill = 'blue')

root.mainloop()
