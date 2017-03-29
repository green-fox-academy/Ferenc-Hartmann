from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


#draw = [[10, 10], [290,  10], [290, 290], [10, 290]]
draw = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]

print(draw[0])
print(draw[1])
draw_line = canvas.create_line(draw[0], draw[1], fill='blue')


root.mainloop()
