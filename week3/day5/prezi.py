import time
from tkinter import*
root = Tk()
canvas = Canvas(root, width='1340', height='700', bg='white')
canvas.pack()

#canvas.create_polygon([150,40, 450,40, 600,300, 450,560, 150,560, 0,300], outline='black', width=2, fill='light blue')
canvas.create_rectangle(0, 0, 670, 350, outline='black', fill='Light Goldenrod', width=2)
canvas.create_rectangle(670, 0, 1340, 350, outline='black', fill='black', width=2)
canvas.create_rectangle(0, 350, 670, 700, outline='black', fill='pink', width=2)
canvas.create_rectangle(670, 350, 1340, 700, outline='black', fill='Beige', width=2)

def behindhexadrawer(x, y, size):
    points=[x,y, x+size/2,y, x+3/4*size,y+260/600*size, x+size/2,y+520/600*size, x,y+520/600*size, x-size/4,y+260/600*size]
    canvas.create_polygon(points, outline='black', width=1, fill='black')
behindhexadrawer(250, 40, 300)


def largehexadrawer(x, y, size):
    points=[x,y, x+size/2,y, x+3/4*size,y+260/600*size, x+size/2,y+520/600*size, x,y+520/600*size, x-size/4,y+260/600*size]
    canvas.create_polygon(points, outline='Light Goldenrod', width=1, fill='')
def smallhexadrawer(x, y, size):
    points=[x,y, x+size/2,y, x+3/4*size,y+260/600*size, x+size/2,y+520/600*size, x,y+520/600*size, x-size/4,y+260/600*size]
    canvas.create_polygon(points, outline='Light Goldenrod', width=1, fill='Light Goldenrod')

def drawlargetriangle(x, y, size):
    points=[x,y, x+size, y, x+1/2*size,y+520/600*size,]
    canvas.create_polygon(points, outline='black', width=1, fill='pink')
def drawsmalltriangle(x, y, size):
    points=[x,y, x+size, y, x+1/2*size,y+520/600*size,]
    canvas.create_polygon(points, outline='black', width=1, fill='black')

def recursive_hexa(x, y, size):
    largehexadrawer(x+100, y, size)
    #time.sleep(0.03)
    #canvas.update()
    if size > 25:
        recursive_hexa(x,y, size*1/2)
        recursive_hexa(x+size*225/600,y+size*130/600, size*1/2)
        recursive_hexa(x,y+size*260/600, size*1/2)
    if 25 > size > 10:
        smallhexadrawer(x+100, y, size)
        recursive_hexa(x,y, size*1/2)
        recursive_hexa(x+size*225/600,y+size*130/600, size*1/2)
        recursive_hexa(x,y+size*260/600, size*1/2)

def recursive_triangle(x, y, size):
    #time.sleep(0.03)
    #canvas.update()
    if size > 15:
        drawlargetriangle(x, y, size)
        recursive_triangle(x, y, size*1/2)
        recursive_triangle(x+size/2,y, size*1/2)
        recursive_triangle(x+size/4,y+260/600*size, size*1/2)
    if 15 > size > 5:
        drawsmalltriangle(x, y, size)
        recursive_triangle(x, y, size*1/2)
        recursive_triangle(x+size/2,y, size*1/2)
        recursive_triangle(x+size/4,y+260/600*size, size*1/2)


def advanceddraw():
    recursive_hexa(150, 40, 300)
    recursive_triangle(870, 50, 300)
advanceddraw()

root.mainloop()
