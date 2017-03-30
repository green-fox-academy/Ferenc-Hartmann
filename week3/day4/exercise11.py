import time
from tkinter import*
root = Tk()
canvas = Canvas(root, width='600', height='600', bg='yellow')
canvas.pack()

def drawsquare(x, y, size):
    canvas.create_rectangle(x, y, x+size, y+size, outline='black', width=1)

def recursive_sg(x, y, size):
    drawsquare(x, y, size)
    time.sleep(0.1)
    canvas.update()
    if size > 5:
        recursive_sg(size/3+x, y, size/3)
        recursive_sg(x + 2/3*size, y+size/3, size/3)
        recursive_sg(x, y + 1/3*size, size/3)
        recursive_sg(x + 1/3*size, y + 2/3*size, size/3)

recursive_sg(10, 10, 550)




root.mainloop()
