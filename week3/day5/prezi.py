import time
from tkinter import*
root = Tk()
canvas = Canvas(root, width='1340', height='700', bg='white')
canvas.pack()

def firstpic():
    pic = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week3\day5\firstpic.png")
    item = canvas.create_image(675, 400, image=pic)
    time.sleep(1)
    canvas.update()
firstpic()
time.sleep(5)
canvas.update()

pic = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week3\day5\firstpic.png")
picture = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week3\day5\bulldozer_prezi.png")

def bulldozer(x, y, size):
    item = canvas.create_image(675, 400, image=pic)
    canvas.create_rectangle(x-1340, 0, x+size, 700, outline='white', fill='white', width=2)
    item = canvas.create_image(x+200, 350, image=picture)

def movingbulldozer(x, y, size):
    bulldozer(x, y, size)
    time.sleep(0.03)
    canvas.update()
    if (x+size) < 1400:
       movingbulldozer(x+size, y, size)

movingbulldozer(0, 0, 15)
time.sleep(1)
canvas.update()

canvas.create_rectangle(0, 0, 670, 350, outline='black', fill='Light Goldenrod', width=2)
canvas.create_rectangle(670, 0, 1340, 350, outline='black', fill='black', width=2)
canvas.create_rectangle(0, 350, 670, 700, outline='black', fill='black', width=2)
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

def drawlargehexa2(x, y, size):
    points=[x,y, x+size/2,y, x+3/4*size,y+260/600*size, x+size/2,y+520/600*size, x,y+520/600*size, x-size/4,y+260/600*size]
    canvas.create_polygon(points, fill='Antique White')

def drawsmallhexa2(x, y, size):
    points=[x,y, x+size/2,y, x+3/4*size,y+260/600*size, x+size/2,y+520/600*size, x,y+520/600*size, x-size/4,y+260/600*size]
    canvas.create_polygon(points, outline='black', width=1, fill='black')

def recursive_hexa(x, y, size):
    largehexadrawer(x+100, y, size)
    time.sleep(0.03)
    canvas.update()
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
    time.sleep(0.03)
    canvas.update()
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

def recursive_hexa2(x, y, size):
    time.sleep(0.03)
    canvas.update()
    if size > 30:
        drawlargehexa2(x+100, y+350, size)
        recursive_hexa2(x+size/3,y, size*1/3)
        recursive_hexa2(x+size/3,y+260/600*4/3*size, size*1/3)
        recursive_hexa2(x-size/8*4/3,y+130/600*4/3*size, size*1/3)
        recursive_hexa2(x,y, size*1/3)
        recursive_hexa2(x+size*225/600*4/3,y+size*130/600*4/3, size*1/3)
        recursive_hexa2(x,y+size*260/600*4/3, size*1/3)
    if 30 > size > 10:
        drawsmallhexa2(x+100, y+350, size)
        recursive_hexa2(x+size/3,y, size*1/3)
        recursive_hexa2(x+size/3,y+260/600*4/3*size, size*1/3)
        recursive_hexa2(x-size/8*4/3,y+130/600*4/3*size, size*1/3)
        recursive_hexa2(x,y, size*1/3)
        recursive_hexa2(x+size*225/600*4/3,y+size*130/600*4/3, size*1/3)
        recursive_hexa2(x,y+size*260/600*4/3, size*1/3)



def advanceddraw():
    recursive_hexa(150, 40, 300)
    recursive_triangle(870, 50, 300)
    behindhexadrawer(250, 390, 300)
    recursive_hexa2(150, 40, 300)
advanceddraw()

root.mainloop()
