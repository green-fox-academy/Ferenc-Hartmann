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





def move():
    x=0
    item2 = canvas.create_image(x+20, 350, image=test_tank_pic)
    item3 = canvas.create_image(1326 - x, 350, image=test_tank_pic)

    while x<501:
        canvas.delete(item2, item3)
        item2 = canvas.create_image(x+20, 350, image=test_tank_pic)
        item3 = canvas.create_image(1326 - x, 350, image=test_tank_pic)
        x = x+3
        canvas.move(item2, 3, 0)
        if x % 10 == 0:
            time.sleep(0.3)
        time.sleep(0.03)
        if  x > 495:
            item4 = 0
            health = 10
            while health > 0:
                health-=2
                x=0
                while x < 276:
                    x += 276/8
                    item4 = canvas.create_image((x+20), 350, image=projectile)
                    canvas.move(item4, 276/8, 0)
                    time.sleep(0.03)
                    canvas.update()
                canvas.lower(item4)
                canvas.lower(item4)
                canvas.update()
                time.sleep(1.5)
            canvas.update()
            canvas.lower(item3)

            canvas.update()
move()



root.mainloop()
