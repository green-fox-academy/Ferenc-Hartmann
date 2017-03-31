import time
from tkinter import*
root = Tk()
canvas = Canvas(root, width='600', height='600', bg='blue')
canvas.pack()

#canvas.create_line(300, 600, 300, 570, width=1, fill='yellow')
#canvas.create_line(300, 570, 300, 540, width=1, fill='yellow')
#canvas.create_line(300, 600, 300, 570, width=1, fill='yellow')


def drawline(x, y, size):
    canvas.create_line(x, y, x, y-size/20, width=1, fill='yellow')
    canvas.create_line(x, y, x+size/20, y-size/20, width=1, fill='yellow')
    canvas.create_line(x, y, x-size/20, y-size/20, width=1, fill='yellow')

def recursive_tree(x, y, size):
    n = 1
    drawline(x, y, size)
    time.sleep(0.1)
    canvas.update()
    if size > 10:
        n*recursive_tree(x,y-size/20, size*0.9)
        n +=2
recursive_tree(300, 600, 600)




root.mainloop()
