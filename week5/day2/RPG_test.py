import time
import vlc
from tkinter import*
root = Tk()
canvas = Canvas(root, width='720', height='720', bg='white')
#canvas.pack()

class Tile():
    def __init__(self):
        self.floor = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\floor.png")
        self.wall = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\wall.png")
        self.hero_left = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-left.png")
        self.hero_right = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-right.png")
        self.hero_up = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-up.png")
        self.hero_down = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-down.png")
        self.char_x = 0
        self.char_y = 0
        self.char_move = 0

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

        self.hero = canvas.create_image(36, 36, image=self.hero_down)

    def hero_draw(self):
        canvas.delete(self.hero)
        if self.char_move == 1:
            self.char_y -= 72
        if self.char_move == 2:
            self.char_y += 72
        if self.char_move == 3:
            self.char_y -= 72
        if self.char_move == 4:
            self.char_y -= 72

        self.hero = canvas.create_image(36 + self.char_x, 36 + self.char_y, image=self.hero_down)
        canvas.update

class Game_Logic(Tile):
    def __init__(self):
        canvas.bind("<KeyPress>", self.char_move_check)

    def char_move_check(self, e):
        self.e = e
        if self.e.keycode == 38:
            up_case = 0
            for i in range(len(self.wall_tile)):
                if ((self.char_x) // 72) == self.wall_tile[i][0] and ((self.char_y - 72) // 72) == self.wall_tile[i][1] or ((self.char_y - 72) // 72) == -1:
                    up_case +=1
            if up_case == 0:
                self.char_move = 1
        elif self.e.keycode == 40:
            down_case = 0
            for i in range(len(self.wall_tile)):
                if ((self.char_x) // 72) == self.wall_tile[i][0] and ((self.char_y + 72) // 72) == self.wall_tile[i][1] or ((self.char_y + 72) // 72) == 10:
                    down_case +=1
            if down_case == 0:
                self.char_move = 2
        elif self.e.keycode == 37:
            left_case = 0
            for i in range(len(self.wall_tile)):
                if ((self.char_x - 72) // 72) == self.wall_tile[i][0] and ((self.char_y) // 72) == self.wall_tile[i][1] or ((self.char_x - 72) // 72) == -1:
                    left_case +=1
            if left_case == 0:
                self.char_move = 3
        elif self.e.keycode == 39:
            right_case = 0
            for i in range(len(self.wall_tile)):
                if ((self.char_x + 72) // 72) == self.wall_tile[i][0] and ((self.char_y) // 72) == self.wall_tile[i][1] or ((self.char_x + 72) // 72) == 10:
                    right_case +=1
            if right_case == 0:
                self.char_move = 4
        self.hero_draw()



canvas.pack()
canvas.focus_set()


alma = Tile()
alma.map_draw()

root.mainloop()
