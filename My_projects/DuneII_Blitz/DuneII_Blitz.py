#DuneII Blitz created by Ferenc Hartmann
import time
from tkinter import*
root = Tk()
root.attributes('-fullscreen', True)
canvas = Canvas(root, width='1366', height='768', bg='white')
canvas.pack()
root = Tk()

def loadscreen():
    pic = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune1.png")
    item = canvas.create_image(683, 384, image=pic)
#    time.sleep(5)
    canvas.update()

loadscreen()
time.sleep(5)
canvas.update()



root.mainloop()
