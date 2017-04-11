import time
from tkinter import*
root = Tk()
canvas = Canvas(root, width='720', height='720', bg='white')

class Tile():
    def __init__(self):
        self.floor = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\floor.png")
        self.wall = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\wall.png")
        self.hero_left = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-left.png")
        self.hero_right = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-right.png")
        self.hero_up = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-up.png")
        self.hero_down = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-down.png")
        self.skeleton = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\skeleton.png")
        self.boss = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\boss.png")
        canvas.bind("<KeyPress>", self.hero_draw)
        self.char_x = 0
        self.char_y = 0
        self.move_counter = 0
        self.monster_x = 0
        self.monster_y = 0

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
        self.skeleton1 = canvas.create_image(36 + 72 * 4, 36, image=self.skeleton)
        self.skeleton2 = canvas.create_image(36 + 72 * 9, 36 + 72 * 2, image=self.skeleton)
        self.skeleton3 = canvas.create_image(36 + 72 * 0, 36 + 72 * 5, image=self.skeleton)
        self.skeleton4 = canvas.create_image(36 + 72 * 7, 36 + 72 * 8, image=self.skeleton)
        self.boss1 = canvas.create_image(36 + 72 * 2, 36 + 72 * 9, image=self.boss)

    def hero_draw(self, e):
        self.e = e
        canvas.delete(self.hero)
        if self.e.keycode == 38:
            self.up_case = 0
            for i in range(len(self.wall_tile)):
                if ((self.char_x) // 72) == self.wall_tile[i][0] and ((self.char_y - 72) // 72) == self.wall_tile[i][1] or ((self.char_y - 72) // 72) == -1:
                    self.up_case +=1
            if self.up_case == 0:
                self.char_y -= 72
                self.move_counter += 1
                self.sekelton_draw()
        elif self.e.keycode == 40:
            self.down_case = 0
            for i in range(len(self.wall_tile)):
                if ((self.char_x) // 72) == self.wall_tile[i][0] and ((self.char_y + 72) // 72) == self.wall_tile[i][1] or ((self.char_y + 72) // 72) == 10:
                    self.down_case +=1
            if self.down_case == 0:
                self.char_y += 72
                self.move_counter += 1
                self.sekelton_draw()
        elif self.e.keycode == 37:
            self.left_case = 0
            for i in range(len(self.wall_tile)):
                if ((self.char_x - 72) // 72) == self.wall_tile[i][0] and ((self.char_y) // 72) == self.wall_tile[i][1] or ((self.char_x - 72) // 72) == -1:
                    self.left_case +=1
            if self.left_case == 0:
                self.char_x -= 72
                self.move_counter += 1
                self.sekelton_draw()
        elif self.e.keycode == 39:
            self.right_case = 0
            for i in range(len(self.wall_tile)):
                if ((self.char_x + 72) // 72) == self.wall_tile[i][0] and ((self.char_y) // 72) == self.wall_tile[i][1] or ((self.char_x + 72) // 72) == 10:
                    self.right_case +=1
            if self.right_case == 0:
                self.char_x += 72
                self.move_counter += 1
                self.sekelton_draw()

        if self.e.keycode == 38:
            self.hero = canvas.create_image(36 + self.char_x, 36 + self.char_y, image=self.hero_up)
        elif self.e.keycode == 40:
            self.hero = canvas.create_image(36 + self.char_x, 36 + self.char_y, image=self.hero_down)
        elif self.e.keycode == 37:
            self.hero = canvas.create_image(36 + self.char_x, 36 + self.char_y, image=self.hero_left)
        elif self.e.keycode == 39:
            self.hero = canvas.create_image(36 + self.char_x, 36 + self.char_y, image=self.hero_right)

        canvas.update

    def sekelton_draw(self):
        if self.move_counter % 2 == 0 and self.move_counter != 0:
            canvas.delete(self.skeleton1, self.skeleton2, self.skeleton3, self.skeleton4, self.boss1)
            if self.move_counter % 8 == 2 or self.move_counter % 8 == 4:
                self.monster_x += 1
                self.monster_y += 1
            if self.move_counter % 8 == 6 or self.move_counter % 8 == 0:
                self.monster_x -= 1
                self.monster_y -= 1
            print(self.monster_x)
            print(self.monster_y)
            print(self.move_counter)

            self.skeleton1 = canvas.create_image(36 + 72 * 4, 36 + 72 * (0 + self.monster_y), image=self.skeleton)
            self.skeleton2 = canvas.create_image(36 + 72 * 9, 36 + 72 * (2 + self.monster_y), image=self.skeleton)
            self.skeleton3 = canvas.create_image(36 + 72 * 0, 36 + 72 * (5 + self.monster_y), image=self.skeleton)
            self.skeleton4 = canvas.create_image(36 + 72 * (7 - self.monster_x), 36 + 72 * 8, image=self.skeleton)
            self.boss1 = canvas.create_image(36 + 72 * (2 - self.monster_x), 36 + 72 * 9, image=self.boss)





canvas.pack()
canvas.focus_set()


alma = Tile()
alma.map_draw()

root.mainloop()
