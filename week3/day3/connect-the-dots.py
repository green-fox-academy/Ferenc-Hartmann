
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

def linedrawer():
    x = input("please enter box or fox to choose a drawing: ")
    if str(x) == "box":
        draw = [[10, 10], [290,  10], [290, 290], [10, 290]]
        draw.append(draw[0])
    if str(x) == "fox":
        draw = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]
    for i in range(len(draw)):
        if i == len(draw):
            draw_line = canvas.create_line(draw[i][0], draw[i][1], draw[0][0], draw[0][1], fill='blue')
        if (i) < (len(draw) - 1):
            draw_line = canvas.create_line(draw[i][0], draw[i][1], draw[i+1][0], draw[i+1][1], fill='blue')

linedrawer()
root.mainloop()
