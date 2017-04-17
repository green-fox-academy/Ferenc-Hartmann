from tkinter import*
import random
import vlc
root = Tk()
root.attributes('-fullscreen', True)
canvas = Canvas(root, width='1214', height='718', bg='white')

#image = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\prezi1.png")
#item = canvas.create_image(683, 384, image=image)
#user_input_1 = input("")

class Tile():
    def __init__(self):
        self.game_over = Button(width=30, height=4, fg="red", bg="black", text=r"You died. Game Over.", font=("Harrington",45,"bold"), command=root.quit)
        self.game_win = Button(width=30, height=4, fg="gold", bg="white", text=r"You win the game!", font=("Harrington",45,"bold"), command=root.quit)
        self.floor = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\floor.png")
        self.wall = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\wall.png")
        self.hero_left = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-left.png")
        self.hero_right = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-right.png")
        self.hero_up = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-up.png")
        self.hero_down = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\hero-down.png")
        self.skeleton = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\skeleton.png")
        self.boss = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\boss.png")
        self.sidepic = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\week5\day2\images\rpg.png")
        canvas.bind("<KeyPress>", self.main_logic)
        self.char_x = 0
        self.char_y = 0
        self.move_counter = 0
        self.monster_x = 0
        self.monster_y = 0
        self.space_counter = 0
        self.space_counter_max = 0
        self.monster_id = 0
        self.dead_switch1 = 0
        self.dead_switch2 = 0
        self.dead_switch3 = 0
        self.dead_switch4 = 0
        self.dead_switch5 = 0
        self.hp_resetter = 0
        self.hero_max_hp = 20 + 3 * random.randrange(1,6)
        self.hero_cur_hp = self.hero_max_hp
        self.hero_dp = 2 * random.randrange(1,6)
        self.hero_sp = 5 + random.randrange(1,6)
        self.hero_level = 1
        self.map_level = 1
        self.hero_hud()

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
        self.skeleton2 = canvas.create_image(36 + 72 * 9, 36 + 72 * 4, image=self.skeleton)
        self.skeleton3 = canvas.create_image(36 + 72 * 0, 36 + 72 * 5, image=self.skeleton)
        self.skeleton4 = canvas.create_image(36 + 72 * 7, 36 + 72 * 8, image=self.skeleton)
        self.boss1 = canvas.create_image(36 + 72 * 9, 36 + 72 * 0, image=self.boss)
        self.picture = canvas.create_image(720, 500, image=self.sidepic, anchor=W)
        self.soundplayer(r"C:\Greenfox\Ferenc-Hartmann\week5\day2\audio.mp3")

    def soundplayer(self, music):
        self.pp = vlc.MediaPlayer(music)
        self.pp.play()

    def create_monster_stats(self):
        self.monster_level_calculator = random.random()

        if self.monster_level_calculator < 0.5:
            self.monster_level = self.map_level
        if 0.9 > self.monster_level_calculator > 0.5:
            self.monster_level = self.map_level + 1
        if self.monster_level_calculator > 0.9:
            self.monster_level = self.map_level + 2

        self.monster1_max_hp = + 2 * self.monster_level * random.randrange(1,6)
        self.monster1_cur_hp = self.monster1_max_hp
        self.monster1_dp = self.monster_level / 2 * random.randrange(1,6)
        self.monster1_sp = self.monster_level * random.randrange(1,6)

        self.monster2_max_hp = + 2 * self.monster_level * random.randrange(1,6)
        self.monster2_cur_hp = self.monster2_max_hp
        self.monster2_dp = self.monster_level / 2 * random.randrange(1,6)
        self.monster2_sp = self.monster_level * random.randrange(1,6)

        self.monster3_max_hp = 2 * self.monster_level * random.randrange(1,6)
        self.monster3_cur_hp = self.monster3_max_hp
        self.monster3_dp = self.monster_level / 2 * random.randrange(1,6)
        self.monster3_sp = self.monster_level * random.randrange(1,6)

        self.monster4_max_hp = 2 * self.monster_level * random.randrange(1,6)
        self.monster4_cur_hp = self.monster4_max_hp
        self.monster4_dp = self.monster_level / 2 * random.randrange(1,6)
        self.monster4_sp = self.monster_level * random.randrange(1,6)

        self.monster5_max_hp = 2 * self.monster_level * random.randrange(1,6) + random.randrange(1,6)
        self.monster5_cur_hp = self.monster5_max_hp
        self.monster5_dp = self.monster_level / 2 * random.randrange(1,6) + 1 / 2 * random.randrange(1,6)
        self.monster5_sp = self.monster_level * random.randrange(1,6) + self.monster_level

    def main_logic(self, e):
        self.e = e
        self.case = 0
        for i in range(len(self.wall_tile)):
            if self.e.keycode == 38 and \
             ((self.char_x) // 72) == self.wall_tile[i][0] and \
             ((self.char_y - 72) // 72) == self.wall_tile[i][1] or \
             ((self.char_y - 72) // 72) == -1 and \
             self.e.keycode == 38:
                self.case = 1
            if self.e.keycode == 40 and \
            ((self.char_x) // 72) == self.wall_tile[i][0] and \
            ((self.char_y + 72) // 72) == self.wall_tile[i][1] or \
            ((self.char_y + 72) // 72) == 10 and \
            self.e.keycode == 40:
                self.case = 2
            if self.e.keycode == 37 and \
            ((self.char_x - 72) // 72) == self.wall_tile[i][0] and \
            ((self.char_y) // 72) == self.wall_tile[i][1] or \
            ((self.char_x - 72) // 72) == -1 and \
            self.e.keycode == 37:
                self.case = 3
            if self.e.keycode == 39 and \
            ((self.char_x + 72) // 72) == self.wall_tile[i][0] and \
            ((self.char_y) // 72) == self.wall_tile[i][1] or \
            ((self.char_x + 72) // 72) == 10 and \
            self.e.keycode == 39:
                self.case = 4

        if self.e.keycode == 38:
            if self.case == 0:
                self.char_y -= 72
                self.move_counter += 1
                self.npc_move()
            canvas.delete(self.hero)
            self.hero = canvas.create_image(36 + self.char_x, 36 + self.char_y, image=self.hero_up)
        elif self.e.keycode == 40:
            if self.case == 0:
                self.char_y += 72
                self.move_counter += 1
                self.npc_move()
            canvas.delete(self.hero)
            self.hero = canvas.create_image(36 + self.char_x, 36 + self.char_y, image=self.hero_down)
        elif self.e.keycode == 37:
            if self.case == 0:
                self.char_x -= 72
                self.move_counter += 1
                self.npc_move()
            canvas.delete(self.hero)
            self.hero = canvas.create_image(36 + self.char_x, 36 + self.char_y, image=self.hero_left)
        elif self.e.keycode == 39:
            if self.case == 0:
                self.char_x += 72
                self.move_counter += 1
                self.npc_move()
            canvas.delete(self.hero)
            self.hero = canvas.create_image(36 + self.char_x, 36 + self.char_y, image=self.hero_right)

        if self.e.keycode == 32:
            self.space_counter += 1

        self.battle_coordinator()

    def npc_move(self):
        canvas.delete(self.skeleton1, self.skeleton2, self.skeleton3, self.skeleton4, self.boss1)
        if self.move_counter % 2 == 0 and self.move_counter != 0:
            if self.move_counter % 12 == 2 or self.move_counter % 12 == 4 or self.move_counter % 12 == 6:
                self.monster_x += 1
                self.monster_y += 1
            if self.move_counter % 12 == 8 or self.move_counter % 12 == 10 or self.move_counter % 12 == 0:
                self.monster_x -= 1
                self.monster_y -= 1

        if self.dead_switch1 == 0:
            self.skeleton1 = canvas.create_image(324, 36 + 72 * (0 + self.monster_y), image=self.skeleton)
        if self.dead_switch2 == 0:
            self.skeleton2 = canvas.create_image(684, 36 + 72 * (4 + self.monster_y), image=self.skeleton)
        if self.dead_switch3 == 0:
            self.skeleton3 = canvas.create_image(36, 36 + 72 * (5 + self.monster_y), image=self.skeleton)
        if self.dead_switch4 == 0:
            self.skeleton4 = canvas.create_image(36 + 72 * (7 - self.monster_x), 612, image=self.skeleton)
        if self.dead_switch5 == 0:
            self.boss1 = canvas.create_image(36 + 72 * (9 - self.monster_x), 36, image=self.boss)

    def battle_coordinator(self):
        if (36 + self.char_x) == 324 and \
        (36 + self.char_y) == (36 + 72 * (0 + self.monster_y)) and \
        self.dead_switch1 == 0:
            self.monster_max_hp = self.monster1_max_hp
            if self.hp_resetter == 0:
                self.monster_cur_hp = self.monster1_cur_hp
                self.hp_resetter = 1
            elif self.hp_resetter == 1:
                self.monster_cur_hp = self.monster_cur_hp
            self.monster_dp = self.monster1_dp
            self.monster_sp = self.monster1_sp
            self.monster_id = 1
            self.battle_calculation()
            self.monster_hud()
        if (36 + self.char_x) == 684 and \
        (36 + self.char_y) == (36 + 72 * (4 + self.monster_y)) and \
        self.dead_switch2 == 0:
            self.monster_max_hp = self.monster2_max_hp
            if self.hp_resetter == 0:
                self.monster_cur_hp = self.monster2_cur_hp
                self.hp_resetter = 2
            elif self.hp_resetter == 2:
                self.monster_cur_hp = self.monster_cur_hp
            self.monster_dp = self.monster2_dp
            self.monster_sp = self.monster2_sp
            self.monster_id = 2
            self.battle_calculation()
            self.monster_hud()
        if (36 + self.char_x) == 36 and \
        (36 + self.char_y) == (36 + 72 * (5 + self.monster_y)) and \
        self.dead_switch3 == 0:
            self.monster_max_hp = self.monster3_max_hp
            if self.hp_resetter == 0:
                self.monster_cur_hp = self.monster3_cur_hp
                self.hp_resetter = 3
            elif self.hp_resetter == 3:
                self.monster_cur_hp = self.monster_cur_hp
            self.monster_dp = self.monster3_dp
            self.monster_sp = self.monster3_sp
            self.monster_id = 3
            self.battle_calculation()
            self.monster_hud()
        if (36 + self.char_x) == (36 + 72 * (7 - self.monster_x)) and \
        (36 + self.char_y) == 612 and \
        self.dead_switch4 == 0:
            self.monster_max_hp = self.monster4_max_hp
            if self.hp_resetter == 0:
                self.monster_cur_hp = self.monster4_cur_hp
                self.hp_resetter = 4
            elif self.hp_resetter == 4:
                self.monster_cur_hp = self.monster_cur_hp
            self.monster_dp = self.monster4_dp
            self.monster_sp = self.monster4_sp
            self.monster_id = 4
            self.battle_calculation()
            self.monster_hud()
        if (36 + self.char_x) == (36 + 72 * (9 - self.monster_x)) and \
        (36 + self.char_y) == 36 and \
        self.dead_switch5 == 0:
            self.monster_max_hp = self.monster5_max_hp
            if self.hp_resetter == 0:
                self.monster_cur_hp = self.monster5_cur_hp
                self.hp_resetter = 5
            elif self.hp_resetter == 5:
                self.monster_cur_hp = self.monster_cur_hp
            self.monster_dp = self.monster5_dp
            self.monster_sp = self.monster5_sp
            self.monster_id = 5
            self.battle_calculation()
            self.monster_hud()

    def battle_calculation(self):

        if self.space_counter > self.space_counter_max:
            self.space_counter_max = self.space_counter
            strike_value = self.hero_sp + 2 * random.randrange(1,6)
            if strike_value > self.monster_dp:
                self.monster_cur_hp = self.monster_cur_hp - (strike_value - self.monster_dp)
            strike_value2 = self.monster_sp + 2 * random.randrange(1,6)
            if strike_value2 > self.hero_dp:
                self.hero_cur_hp = self.hero_cur_hp - (strike_value2 - self.hero_dp)
                self.hero_hud()

        if self.hero_cur_hp <= 0:
            canvas.delete(self.hero)
            self.game_over.place(relx=0.5, rely=0.5, anchor=CENTER)

        if self.monster_cur_hp <= 0 and self.monster_id == 1:
            canvas.delete(self.skeleton1)
            self.dead_switch1 = 1
            self.hp_resetter = 0
            self.no_hud()
        if self.monster_cur_hp <= 0 and self.monster_id == 2:
            canvas.delete(self.skeleton2)
            self.dead_switch2 = 1
            self.hp_resetter = 0
            self.no_hud()
        if self.monster_cur_hp <= 0 and self.monster_id == 3:
            canvas.delete(self.skeleton3)
            self.dead_switch3 = 1
            self.hp_resetter = 0
            self.no_hud()
            self.win_condition()
        if self.monster_cur_hp <= 0 and self.monster_id == 4:
            canvas.delete(self.skeleton4)
            self.dead_switch4 = 1
            self.hp_resetter = 0
            self.no_hud()
        if self.monster_cur_hp <= 0 and self.monster_id == 5:
            canvas.delete(self.boss1)
            self.dead_switch5 = 1
            self.hp_resetter = 0
            self.no_hud()
            self.win_condition()

    def win_condition(self):
        if self.dead_switch5 == 1 and self.dead_switch3 == 1:
            self.game_win.place(relx=0.5, rely=0.5, anchor=CENTER)

    def hero_hud(self):
        text_hero = ("Hero (level " + str(self.hero_level) + ")    HP: " + str(self.hero_cur_hp) + r"/" + str(self.hero_max_hp) + r"    |    DP: " + str(self.hero_dp) + r"    |    SP: " + str(self.hero_sp))
        header = Label(canvas, font="Harrington 16 bold", text="Your Hero's stat", fg='black', bg='white')
        hero_text = Label(canvas, font="Harrington 12 bold", text=text_hero, fg='black', bg='white')
        header.pack()
        hero_text.pack()
        canvas.create_window(960, 20, window=header)
        canvas.create_window(960, 70, window=hero_text)

    def monster_hud(self):
        self.text_monster = ("Monster (level " + str(self.monster_level) + ")    HP: " + str(self.monster_cur_hp) + r"/" + str(self.monster_max_hp) + r"    |    DP: " + str(self.monster_dp) + r"    |    SP: " + str(self.monster_sp))
        self.midler = Label(canvas, font="Harrington 16 bold", text="Monster's stat", fg='black', bg='white')
        self.monster_text = Label(canvas, font="Harrington 12 bold", text=self.text_monster, fg='black', bg='white')
        self.midler.pack()
        self.monster_text.pack()
        canvas.create_window(960, 120, window=self.midler)
        canvas.create_window(960, 170, window=self.monster_text)

    def no_hud(self):
        canvas.create_window(1960, 120, window=self.midler)
        canvas.create_window(1960, 170, window=self.monster_text)



canvas.pack()
canvas.focus_set()

alma = Tile()
alma.map_draw()
alma.create_monster_stats()


root.mainloop()
