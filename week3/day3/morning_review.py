from tkinter import *

root = Tk()

canvas = Canvas(root, width='800', height='600')
canvas.pack()

lime_box = canvas.create_rectangle(0, 0, 400, 300, fill = 'limegreen')

points = (0,0, 800,600, 0,600)
polygon = canvas.create_polygon(points, fill = 'yellow')

canvas.create_oval(50,50, 300,300, fill = 'blue')
#oval: size = difference between the two coordinate pairs (like a rectangle between them)
#img = Photoimage(20, 20, file = "pic.png")
#canvas.create_image(0,0, anchor=SW, image=img)

#coord = (20, 20)
#arc = canvas.create_arc(coord, start=0, extent=10, fill='red')

root.mainloop()
