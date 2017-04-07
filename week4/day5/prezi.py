
from tkinter import*
root = Tk()
root.attributes('-fullscreen', True)
canvas = Canvas(root, width='1366', height='768', bg='black')
canvas.pack()
canvas.update()
image = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week4\day5\prezilast.png")
item = canvas.create_image(683, 384, image=image)

root.mainloop()
