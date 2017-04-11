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
        self.hero_left = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-left.png")
        self.hero_right = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-right.png")
        self.hero_up = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-up.png")
        self.hero_down = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-down.png")


    def map_draw(self):
        for x in range(10):
            for y in range(10):
                self.floors = canvas.create_image(36 + 72 * x, 36 + 72 * y, image=self.floor)

        self.wall_tile = [
                        [3, 0], [5, 0],
                        [3, 1], [5, 1], [7, 1], [8, 1],
                        [1, 2], [2, 2], [3, 2], [5, 2], [7, 2], [8, 2],
                        [5, 3],
                        [0, 4], [1, 4], [2, 4], [3, 4], [5, 4], [6, 4], [7, 4], [8, 4],
                        [1, 5], [3, 5], [8, 5],
                        [1, 6], [3, 6], [5, 6], [6, 6], [8, 6],
                        [5, 7], [6, 7], [8, 7],
                        [1, 8], [2, 8], [3, 8], [8, 8],
                        [3, 9], [5, 9], [6, 9],
                        ]

        for i in range(len(self.wall_tile)):
                self.walls = canvas.create_image(36 + 72 * self.wall_tile[i][0], 36 + 72 * self.wall_tile[i][1], image=self.wall)




#        self.hero_left = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-left.png")
#        self.hero_right = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-right.png")
#        self.hero_up = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-up.png")
#        self.hero_down = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-down.png")


        self.hero = canvas.create_image(36, 36, image=self.hero_down)
#    def on_key_press(e):
        # When the keycode is 111 (up arrow) we move the position of our box higher
#        if e.keycode == 38:
#            box.testBoxY = box.testBoxY - 100
#        elif e.keycode == 40:
#            box.testBoxY = box.testBoxY + 100
        # and lower if the key that was pressed the down arrow
        # draw the box again in the new position
#        box.draw(canvas)

    # Tell the canvas that we prepared a function that can deal with the key press events
#    canvas.bind("<KeyPress>", on_key_press)
#    canvas.pack()

    # Select the canvas to be in focused so it actually recieves the key hittings
#    canvas.focus_set()

    # Draw the box in the initial position
#    box.draw(canvas)



alma = Tile()
alma.map_draw()
root.mainloop()
