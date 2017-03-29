from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/line-play/r1.png]

def middrawer():
    for i in range(15):
        top_lines = canvas.create_line(20 * i, 0, 300, 20 * i, fill='orchid')
        bottom_lines = canvas.create_line(0, 20 * i, 20 * i, 300, fill='green')

middrawer()
root.mainloop()
