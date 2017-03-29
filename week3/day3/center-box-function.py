from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.


def centsquaredrawer():

    x1 = input("please enter size of the first box: ")
    x2 = input("please enter size of the first box: ")
    x3 = input("please enter size of the first box: ")

    center_box = canvas.create_rectangle((150 - (int(x1) // 2)), (150 - (int(x1) // 2)), (150 + (int(x1) // 2)), (150 + (int(x1) // 2)), fill = 'light sea green')
    center_box = canvas.create_rectangle((150 - (int(x2) // 2)), (150 - (int(x2) // 2)), (150 + (int(x2) // 2)), (150 + (int(x2) // 2)), fill = 'red')
    center_box = canvas.create_rectangle((150 - (int(x3) // 2)), (150 - (int(x3) // 2)), (150 + (int(x3) // 2)), (150 + (int(x3) // 2)), fill = 'yellow')

centsquaredrawer()
root.mainloop()
