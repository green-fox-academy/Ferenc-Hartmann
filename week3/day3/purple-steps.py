from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/purple-steps/r3.png]


def purplestepper():

    for i in range (20):
        purpleboxes = canvas.create_rectangle(int(i) * 10 + 10, int(i) * 10 + 10, ((int(i) * 10) + 20), ((int(i) * 10) + 20), fill = 'orchid')

purplestepper()
root.mainloop()
