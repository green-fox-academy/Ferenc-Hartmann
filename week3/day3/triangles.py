from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/triangles/r5.png]



def nightdrawer():
    y = 290
    for i in range(0,20):
        horizontal_lines = canvas.create_line(14*i, y, 300-14*i, y, fill='black')
        y -= 3**(.5)*15
nightdrawer()
root.mainloop()
sqrt= 3**(.5)
