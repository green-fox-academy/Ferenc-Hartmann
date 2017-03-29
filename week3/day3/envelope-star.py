from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/envelope-star/r2.png]

def starlinesdrawer():
    for i in range(1,16):
        bottom_left_lines = canvas.create_line(10 * i, 150, 150, 10 * i + 150, fill='green')
        top_left_lines = canvas.create_line(150, 10 * (i-1), 150 - 10 * (i-1), 150, fill='green')
        top_right_lines = canvas.create_line(150, 10 * (i-1), 10 * (i-1) + 150, 150, fill='green')
        bottom_right_lines = canvas.create_line(150, 150 + (10 * i), 300 - (10 * i), 150, fill='green')

starlinesdrawer()
root.mainloop()
