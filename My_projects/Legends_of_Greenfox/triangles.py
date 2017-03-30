from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/triangles/r5.png]



def nightdrawer():
    for i in range(1,21):
        horizontal_lines = canvas.create_line(0, 250, 300, 250, fill='orchid')

nightdrawer()
root.mainloop()
