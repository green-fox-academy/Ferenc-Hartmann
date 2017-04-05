#DuneII Blitz created by Ferenc Hartmann
import time
import random
from tkinter import*
root = Tk()
root.attributes('-fullscreen', True)
canvas = Canvas(root, width='1366', height='768', bg='black')
canvas.pack()
canvas.update()


def loadscreen():
    a = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart10.png")
    b = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart9.png")
    c = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart8.png")
    d = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart7.png")
    e = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart6.png")
    f = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart5.png")
    g = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart4.png")
    h = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart3.png")
    i = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart2.png")
    j = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart1.png")
    pics=[a,b,c,d,e,f,g,h,i,j]

    time.sleep(1)

    for pic in pics:
        loadscreen = canvas.create_image(670, 384, image=pic)
        time.sleep(0.05)
        canvas.update()
        canvas.delete("all")

    time.sleep(1)
    pics=reversed(pics)

    for pic in pics:
        loadscreen = canvas.create_image(670, 384, image=pic)
        time.sleep(0.05)
        canvas.update()
        canvas.delete("all")

loadscreen()
canvas.delete("all")
canvas.update()
time.sleep(1)



load_screen = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune1pro.png")
item = canvas.create_image(683, 384, image=load_screen)

import vlc
p = vlc.MediaPlayer("C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\main_menu.mp3")
p.play()

a = Button(width=20, height=1, fg="white", bg="black", text="Start New Game", font=("Harrington",30,"bold"))
b = Button(width=20, height=1, fg="white", bg="black", text="Load Game", font=("Harrington",30,"bold"))
c = Button(width=20, height=1, fg="white", bg="black", text="Help", font=("Harrington",30,"bold"))
d = Button(width=20, height=1, fg="white", bg="black", text="Quit", font=("Harrington",30,"bold"), command = root.quit)

a.place(relx=0.5, y=400, anchor=CENTER)
b.place(relx=0.5, y=500, anchor=CENTER)
c.place(relx=0.5, y=600, anchor=CENTER)
d.place(relx=0.5, y=700, anchor=CENTER)






root.mainloop()
