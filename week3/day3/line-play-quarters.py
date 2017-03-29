
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/line-play/r1.png]

def happylinesdrawer():
    for k in range(2):
        for j in range(2):
            for i in range(15):
                top_lines = canvas.create_line(10 * i + 150 * j, 150 * k, 150 + 150 * j, 10 * i + 150 * k, fill='orchid')
                bottom_lines = canvas.create_line(150 * j, 10 * i + 150 * k, 10 * i + 150 * j, 150 + 150 * k, fill='green')
happylinesdrawer()
root.mainloop()
