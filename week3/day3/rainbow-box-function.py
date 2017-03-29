from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.

# create a loop that fills the canvas with rainbow colored squares.

def colorcentsquaredrawer():

    x1 = input("please enter size of the first box: ")
    y1 = input("please enter color of the first box: ")
    n = 0
    k = 0
    colors = ['red', 'orange', 'yellow', 'light green', 'green', 'blue', 'indigo', 'violet']
    for i in range (8):
        n += 1
        k = (8-n)
        bigger_box = canvas.create_rectangle((150 - (int(k) * 20)), (150 - (int(k) * 20)), (150 + (int(k) * 20)), (150 + (int(k) * 20)), fill = colors[i])
    center_box = canvas.create_rectangle((150 - (int(x1) // 2)), (150 - (int(x1) // 2)), (150 + (int(x1) // 2)), (150 + (int(x1) // 2)), fill = str(y1))

colorcentsquaredrawer()
root.mainloop()
