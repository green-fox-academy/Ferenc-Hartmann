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
projectile = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\projectile.png")

def bgmap():
    bgpic = canvas.create_image(675, 400, image=picture)

def movingtank(x, y, size):
    tx = x
    ex = x
    ty = y
    ey = y
    thealth = 10
    tdamage = 3
    ehealth = 10
    edamage = 2
    bgmap()
    if thealth > 0:
        item2 = canvas.create_image(tx + 20, 350, image=test_tank_pic)
    if ehealth > 0:
        item3 = canvas.create_image(1346 - ex, 350, image=test_tank_pic)
    time.sleep(0.02)
    canvas.update()
    canvas.delete("all")
    if (x) < 1346:
        if x % 10 == 0:
            time.sleep(0.3)
            if  (1346 - ex) - (tx + 20) <= 200:
                while thealth > 0 and ehealth > 0:
                    item4 = canvas.create_image((tx+20) + ((tx + 20)-(1346 - ex))//(size//3), 350, image=projectile)
                    thealth -= edamage
                    ehealth -= tdamage
                    time.sleep(1)
                    movingtank(x+size, y, size)

#                time.sleep(3)
            else:
                movingtank(x+size, y, size)
        else:
            movingtank(x+size, y, size)





movingtank(0, 0, 3)
time.sleep(5)








root.mainloop()
