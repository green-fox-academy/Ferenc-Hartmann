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


picture = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\map1.png")
test_tank_pic = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\testtank.png")
projectile = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\projectile.png")

def bgmap():
    bgpic = canvas.create_image(675, 400, image=picture)
bgmap()
canvas.update()
item2 = canvas.create_image(20, 350, image=test_tank_pic)
item3 = canvas.create_image(220, 350, image=test_tank_pic)
item4 = 0
health = 10
while health > 0:
    health-=2
    x=0
    while x < (220-40):
        x += (220-40)/8
        canvas.delete(item4)
        item4 = canvas.create_image((x+20), 350, image=projectile)
        canvas.move(item4, (220-40)/8, 0)
        time.sleep(0.03)
        canvas.update()
    canvas.lower(item4)
    canvas.lower(item4)
    canvas.update()
    time.sleep(1.5)
canvas.update()
canvas.lower(item3)
root.mainloop()
