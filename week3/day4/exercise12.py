import time
from tkinter import*
root = Tk()
canvas = Canvas(root, width='600', height='600', bg='white')
canvas.pack()

canvas.create_polygon([150,40, 450,40, 600,300, 450,560, 150,560, 0,300], outline='black', width=2, fill='light blue')
canvas.create_oval(0, 0, 600, 600, outline='yellow', width=2)


def drawhexa(x, y, size):
    points=[x,y, x+size/2,y, x+3/4*size,y+260/600*size, x+size/2,y+520/600*size, x,y+520/600*size, x-size/4,y+260/600*size]
    canvas.create_polygon(points, outline='black', width=1, fill='')
300
def recursive_sg(x, y, size):
    drawhexa(x, y, size)
    time.sleep(0.1)
    canvas.update()
    if size > 10:
        recursive_sg(x,y, size*1/2)
        recursive_sg(x+size*225/600,y+size*130/600, size*1/2)
        recursive_sg(x,y+size*260/600, size*1/2)

recursive_sg(150, 40, 600)




root.mainloop()
