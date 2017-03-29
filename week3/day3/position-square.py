from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

def squaredrawer():

    x1 = input("please enter first square top-left point x parameter: ")
    y1 = input("please enter first square top-left point y parameter: ")
    x2 = input("please enter second square top-left point x parameter: ")
    y2 = input("please enter second square top-left point y parameter: ")
    x3 = input("please enter third square top-left point x parameter: ")
    y3 = input("please enter third square top-left point y parameter: ")

    first_square = canvas.create_rectangle(x1, y1, (int(x1) + 50), (int(y1) + 50), fill='yellow')
    second_square = canvas.create_rectangle(x2, y2, (int(x2) + 50), (int(y2) + 50), fill='green')
    third_square = canvas.create_rectangle(x3, y3, (int(x3) + 50), (int(y3) + 50), fill='red')

squaredrawer()
root.mainloop()
