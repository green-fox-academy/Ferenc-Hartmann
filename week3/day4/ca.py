import time
from tkinter import*
root = Tk()
canvas = Canvas(root, width='600', height='600')
canvas.pack()



def drawsquare(x, y, size):
    canvas.create_rectangle(x, y, x+size, y+size, outline='green', width=2)


def recursive_sg(x, y, size):
    drawsquare(x, y, size)
    time.sleep(0.1)
    canvas.update()
    if size > 20:
        recursive_sg(x, y, size/3)
        recursive_sg(x + 2/3*size, y, size/3)
        recursive_sg(x, y + 2/3*size, size/3)
        recursive_sg(x + 2/3*size, y + 2/3*size, size/3)

recursive_sg(10, 10, 500)


def draw_oval(x, y, size):
    canvas.create_oval(x, y, x+size, y+size, outline='green', width=2)


def recursive_sg(x, y, size):
    draw_oval(x, y, size)
    time.sleep(0.1)
    canvas.update()
    if size > 20:
        recursive_sg(x, y, size/3)
        recursive_sg(x + 2/3*size, y, size/3)
        recursive_sg(x, y + 2/3*size, size/3)
        recursive_sg(x + 2/3*size, y + 2/3*size, size/3)

recursive_sg(10, 10, 500)



root.mainloop()
