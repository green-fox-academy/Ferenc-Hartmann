import time
import vlc
from tkinter import*
root = Tk()
canvas = Canvas(root, width='720', height='720', bg='white')
canvas.pack()

class Tile():
    def __init__(self):
        self.floor = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\floor.png")
        self.wall = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\wall.png")


    def map_draw(self):
        for x in range(10):
            for y in range(10):
                self.floors = canvas.create_image(36 + 72 * x, 36 + 72 * y, image=self.floor)


    def wall_tiles(self):
        self.walls = [[4, 0], [6, 0],
                     [4, 1], [6, 1], [8, 1], [9, 1],
                     [1, 2], [2, 2], [3, 2], [5, 2], [8, 2], [9, 2]
                     [5, 3]]




        for x in range(10):
            self.floors = canvas.create_image(36 + 72 * x, 36, image=self.floor)
            for y in range(10):
                self.floors = canvas.create_image(36 + 72 * x, 36 + 72 * y, image=self.floor)

alma = Tile()
alma.map_draw()
root.mainloop()
