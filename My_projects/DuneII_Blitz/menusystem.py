#DuneII Blitz created by Ferenc Hartmann
import time
import random
from tkinter import*
root = Tk()
root.attributes('-fullscreen', True)
canvas = Canvas(root, width='1366', height='768', bg='white')
canvas.pack()

def loadscreen():
    load_screen = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune1.png")
    item = canvas.create_image(683, 384, image=load_screen)
    canvas.update()

loadscreen()
time.sleep(1)
canvas.update()




load_screen = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune1.png")
item = canvas.create_image(683, 384, image=load_screen)



a = Button(width=20, height=1, fg="white", bg="black", text="Start New Game", font=("Harrington",30,"bold"))
b = Button(width=20, height=1, fg="white", bg="black", text="Load Game", font=("Harrington",30,"bold"))
c = Button(width=20, height=1, fg="white", bg="black", text="Help", font=("Harrington",30,"bold"))
d = Button(width=20, height=1, fg="white", bg="black", text="Quit", font=("Harrington",30,"bold"), command = root.quit)

a.place(relx=0.5, y=400, anchor=CENTER)
b.place(relx=0.5, y=500, anchor=CENTER)
c.place(relx=0.5, y=600, anchor=CENTER)
d.place(relx=0.5, y=700, anchor=CENTER)






root.mainloop()
