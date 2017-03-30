from tkinter import*
root = Tk()
canvas = Canvas(root, width='600', height='600', bg='yellow')
canvas.pack()



def drawline1(x, y, size):
    canvas.create_line(x-size/3, 0, x-size/3, size, fill='blue')
def drawline2(x, y, size):
    canvas.create_line(x-size*2/3, 0, x-size*2/3, size, fill='blue')
def drawline3(x, y, size):
    canvas.create_line(x-y, y*1/3, size, y-size*2/3, fill='blue')
def drawline4(x, y, size):
    canvas.create_line(x-y, y*2/3, size, y-size/3, fill='blue')

#drawlines(600,600,600)

def recursive_lines(x, y, size):
    drawline1(x, y, size)
    drawline2(x, y, size)
    drawline3(x, y, size)
    drawline4(x, y, size)

    if size > 20:
        recursive_lines(size*1/3+x/3, y/3, size*1/3)

recursive_lines(600, 600, 600)


root.mainloop()
