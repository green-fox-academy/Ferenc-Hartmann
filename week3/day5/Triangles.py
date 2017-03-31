import time
from tkinter import*
root = Tk()
canvas = Canvas(root, width='600', height='600', bg='black')
canvas.pack()

#canvas.create_polygon([0,0, 600,0, 300, 520], outline='black', width=2, fill='white')


def drawlargetriangle(x, y, size):
    points=[x,y, x+size, y, x+1/2*size,y+520/600*size,]
    canvas.create_polygon(points, outline='black', width=1, fill='black')
def drawsmalltriangle(x, y, size):
    points=[x,y, x+size, y, x+1/2*size,y+520/600*size,]
    canvas.create_polygon(points, outline='black', width=1, fill='white')

def recursive_sg(x, y, size):
    time.sleep(0.03)
    canvas.update()
    if size > 25:
        drawlargetriangle(x, y, size)
        recursive_sg(x, y, size*1/2)
        recursive_sg(x+size/2,y, size*1/2)
        recursive_sg(x+size/4,y+260/600*size, size*1/2)
    if 25 > size > 10:
        drawsmalltriangle(x, y, size)
        recursive_sg(x, y, size*1/2)
        recursive_sg(x+size/2,y, size*1/2)
        recursive_sg(x+size/4,y+260/600*size, size*1/2)

recursive_sg(0, 0, 600)




root.mainloop()
