import time
from tkinter import*
root = Tk()
canvas = Canvas(root, width='600', height='600', bg='white')
canvas.pack()

a=canvas.create_polygon([0,300, 150,40, 450,40, 600,300, 450,560, 150,560], outline='black', width=2, fill='')
canvas.create_oval(0, 0, 600, 600, outline='yellow', width=2)



root.mainloop()
