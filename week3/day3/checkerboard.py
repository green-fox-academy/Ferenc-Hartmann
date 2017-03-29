from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.

def purplestepper():
    x = 0
    y = 0
    for i in range (6):
        if x % 100 == 0:
            for j in range(6):
                if y % 100 == 0:
                    blackbox = canvas.create_rectangle(x, y, x + 50, y + 50, fill = 'black')
                y += 50
        x += 50
        y = 0
    x = 50
    y = 50
    for i in range (6):
        if x % 100 == 50:
            for j in range(6):
                if y % 100 == 50:
                    blackbox = canvas.create_rectangle(x, y, x + 50, y + 50, fill = 'black')
                y += 50
        x += 50
        y = 0

purplestepper()
root.mainloop()
