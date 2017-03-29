from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.


def middrawer():
    x = input("please enter first line x parameter: ")
    y = input("please enter first line y parameter: ")
    for i in range(15):
        top_lines = canvas.create_line(20 * i, 0, 150, 150, fill='blue')
        bottom_lines = canvas.create_line(20 * i, 300, 150, 150, fill='blue')
        left_lines = canvas.create_line(0, 20 * i, 150, 150, fill='blue')
        right_lines = canvas.create_line(300, 20 * i, 150, 150, fill='blue')
    line = canvas.create_line(x, y, 150, 150, fill='red')

middrawer()
root.mainloop()
