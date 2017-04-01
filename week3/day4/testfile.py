import time
from tkinter import*
root = Tk()
canvas = Canvas(root, width='1340', height='700', bg='white')
canvas.pack()
time.sleep(0.03)
canvas.update()

canvas.create_rectangle(0, 0, 670, 350, outline='black', fill='Light Goldenrod', width=2)
canvas.create_rectangle(670, 0, 1340, 350, outline='black', fill='black', width=2)
canvas.create_rectangle(0, 350, 670, 700, outline='black', fill='black', width=2)
canvas.create_rectangle(670, 350, 1340, 700, outline='black', fill='white', width=2)

lastpic = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week3\day5\lastpic.png")
item = canvas.create_image(1000, 550, image=lastpic)

root.mainloop()
