from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.


def hordrawer():

    x1 = input("please enter first line x parameter: ")
    y1 = input("please enter first line y parameter: ")
    x2 = input("please enter second line x parameter: ")
    y2 = input("please enter second line y parameter: ")
    x3 = input("please enter third line x parameter: ")
    y3 = input("please enter third line y parameter: ")

    first_line = canvas.create_line(x1, y1, (int(x1) + 50), y1, fill='yellow')
    second_line = canvas.create_line(x2, y2, (int(x2) + 50), y2, fill='green')
    third_line = canvas.create_line(x3, y3, (int(x3) + 50), y3, fill='red')

hordrawer()
root.mainloop()
