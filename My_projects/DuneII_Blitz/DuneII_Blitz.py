#DuneII Blitz created by Ferenc Hartmann
import time
import random
from tkinter import*
root = Tk()
root.attributes('-fullscreen', True)
canvas = Canvas(root, width='1366', height='768', bg='black')
canvas.pack()
root = Tk()

def loadscreen():
    load_screen = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune1.png")
    item = canvas.create_image(683, 384, image=load_screen)
    canvas.update()

loadscreen()
time.sleep(1)
canvas.update()


picture = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\map1.png")
test_tank_pic = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\testtank.png")

def testtank(x, y, size):
    item1 = canvas.create_image(675, 400, image=picture)
    item2 = canvas.create_image(x + 20, 350, image=test_tank_pic)

def enemytesttank(x, y, size):
    item2 = canvas.create_image(1326 - x, 350, image=test_tank_pic)


def movingtank(x, y, size):
    testtank(x, y, size)
    enemytesttank(x, y, size)
    time.sleep(0.02)
    canvas.update()
    canvas.delete("all")
    if (x) < 1326:
        if x % 10 == 0:
            time.sleep(0.3)
            movingtank(x+size, y, size)
        else:
            movingtank(x+size, y, size)

movingtank(0, 0, 3)
time.sleep(5)








root.mainloop()
