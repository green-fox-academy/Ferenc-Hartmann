from tkinter import*
root = Tk()
canvas = Canvas(root, width='600', height='600')
canvas.pack()



def drawline1(x, y, size):
    canvas.create_line(x*2/3, y-size, x*2/3, size, fill='blue')
def drawline2(x, y, size):
    canvas.create_line(x/3, y-size, x/3, size, fill='blue')
def drawline3(x, y, size):
    canvas.create_line(x-size, y/3, size, y/3, fill='blue')
def drawline4(x, y, size):
    canvas.create_line(x-size, y*2/3, size, y*2/3, fill='blue')


def recursive_lines(x, y, size):
    drawline1(x, y, size)
    drawline2(x, y, size)
    drawline3(x, y, size)
    drawline4(x, y, size)

    if size > 20:
        recursive_lines(x, y, size*1/3)

recursive_lines(600, 600, 600)

#top
canvas.create_line(600/3, 600/3/3, 2*600/3, 600/3/3, fill='blue')
canvas.create_line(600/3, 2*600/3/3, 2*600/3, 2*600/3/3, fill='blue')
canvas.create_line(600/3 + 600/3/3, 0, 600/3 + 600/3/3, 600/3, fill='blue')
canvas.create_line(600/3 + 2*600/3/3, 0, 600/3 + 2*600/3/3, 600/3, fill='blue')

#right
canvas.create_line(600/3+600/3, 600/3+600/3/3, 600/3+2*600/3, 600/3+600/3/3, fill='blue')
canvas.create_line(600/3+600/3, 600/3+2*600/3/3, 600/3+2*600/3, 600/3+2*600/3/3, fill='blue')
canvas.create_line(600/3+600/3 + 600/3/3, 600/3, 600/3+600/3 + 600/3/3, 600/3+600/3, fill='blue')
canvas.create_line(600/3+600/3 + 2*600/3/3, 600/3, 600/3+600/3 + 2*600/3/3, 600/3+600/3, fill='blue')



root.mainloop()
