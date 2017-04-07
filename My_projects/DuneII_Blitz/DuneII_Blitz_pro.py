#DuneII Blitz created by Ferenc Hartmann
import time
import vlc
from tkinter import*
root = Tk()
root.attributes('-fullscreen', True)
canvas = Canvas(root, width='1366', height='768', bg='black')
canvas.pack()
canvas.update()

class Dune2_Blitz():
    def __init__(self):
        self.a = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart10.png")
        self.b = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart9.png")
        self.c = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart8.png")
        self.d = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart7.png")
        self.e = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart6.png")
        self.f = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart5.png")
        self.g = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart4.png")
        self.h = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart3.png")
        self.i = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart2.png")
        self.j = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart1.png")
        self.main_menu = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune1pro.png")
        self.game_bg = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\game_bg.png")

        self.start_new_game_button = Button(width=20, height=1, fg="white", bg="black", text="Start New Game", font=("Harrington",30,"bold"), command = self.start_new_game_button_clicked)
        self.load_saved_game_button = Button(width=20, height=1, fg="white", bg="black", text="Load Saved Game", font=("Harrington",30,"bold"))
        self.help_button = Button(width=20, height=1, fg="white", bg="black", text="Help", font=("Harrington",30,"bold"))
        self.quit_button = Button(width=20, height=1, fg="white", bg="black", text="Quit", font=("Harrington",30,"bold"), command = root.quit)

        self.house_atreides_button = Button(width=15, height=1, fg="blue", bg="black", text="House Atreides", font=("Harrington",30,"bold"), command=self.house_button_clicked)
        self.house_ordos_button = Button(width=15, height=1, fg="green", bg="black", text="House Ordos", font=("Harrington",30,"bold"), command=self.house_button_clicked)
        self.house_harkonnen_button = Button(width=15, height=1, fg="red", bg="black", text="House Harkonnen", font=("Harrington",30,"bold"), command=self.house_button_clicked)
        self.back_button = Button(width=5, height=1, fg="white", bg="black", text="Back", font=("Harrington",30,"bold"), command=self.back_button_clicked)

        self.house_atreides_pic = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\houseatreides.png")
        self.house_ordos_pic = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\houseordos.png")
        self.house_harkonnen_pic = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\househarkonnen.png")

        self.level1_button = Button(width=4, height=1, fg="white", bg="black", text="lvl 1", font=("Harrington",25,"bold"), command=self.back_button_clicked)
        self.level2_button = Button(width=4, height=1, fg="white", bg="black", text="lvl 2", font=("Harrington",25,"bold"), command=self.back_button_clicked)
        self.level3_button = Button(width=4, height=1, fg="white", bg="black", text="lvl 3", font=("Harrington",25,"bold"), command=self.back_button_clicked)
        self.level4_button = Button(width=4, height=1, fg="white", bg="black", text="lvl 4", font=("Harrington",25,"bold"), command=self.back_button_clicked)
        self.level5_button = Button(width=4, height=1, fg="white", bg="black", text="lvl 5", font=("Harrington",25,"bold"), command=self.back_button_clicked)
        self.level6_button = Button(width=4, height=1, fg="white", bg="black", text="lvl 6", font=("Harrington",25,"bold"), command=self.back_button_clicked)
        self.level7_button = Button(width=4, height=1, fg="white", bg="black", text="lvl 7", font=("Harrington",25,"bold"), command=self.back_button_clicked)
        self.level8_button = Button(width=4, height=1, fg="white", bg="black", text="lvl 8", font=("Harrington",25,"bold"), command=self.back_button_clicked)
        self.level9_button = Button(width=4, height=1, fg="white", bg="black", text="lvl 9", font=("Harrington",25,"bold"), command=self.back_button_clicked)
        self.level10_button = Button(width=4, height=1, fg="white", bg="black", text="lvl 10", font=("Harrington",25,"bold"), command=self.back_button_clicked)
        self.level11_button = Button(width=4, height=1, fg="white", bg="black", text="lvl 11", font=("Harrington",25,"bold"), command=self.back_button_clicked)
        self.level12_button = Button(width=4, height=1, fg="white", bg="black", text="lvl 12", font=("Harrington",25,"bold"), command=self.back_button_clicked)
        self.level13_button = Button(width=4, height=1, fg="white", bg="black", text="lvl 13", font=("Harrington",25,"bold"), command=self.back_button_clicked)
        self.level14_button = Button(width=4, height=1, fg="white", bg="black", text="lvl 14", font=("Harrington",25,"bold"), command=self.back_button_clicked)
        self.level15_button = Button(width=4, height=1, fg="white", bg="black", text="lvl 15", font=("Harrington",25,"bold"), command=self.back_button_clicked)

        self.combat_tank_im = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\combat_tank.png")
        self.siege_tank_im = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\siege_tank.png")
        self.rocket_launcher_im = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\rocket_launcher.png")

        self.battle_button = Button(width=8, height=1, fg="white", bg="black", text="Battle", font=("Harrington",30,"bold"), command=self.battle_start)

        self.loadscreens = 0
        self.start_button_int = 0
        self.back_button_int = 0
        self.game_int = 0

#battle
        self.battle_map = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\map1.png")
        self.atreides_combat_tank = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\atreides_combat_tank.png")
        self.projectile_img = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\projectile.png")
        self.battle_start3 = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\battle_starts_3.png")
        self.battle_start2 = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\battle_starts_2.png")
        self.battle_start1 = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\battle_starts_1.png")
        self.explosion1 = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\explosion1.png")
        self.explosion2 = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\explosion2.png")
        self.mission_complete = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\mission_done.png")

        self.tank1 = 0
        self.tank2 = 0
        self.your_health = 10
        self.enemy_health = 10
        self.projectile = 0


    def loadscreen(self):
        self.pics=[self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h,self.i,self.j]
        time.sleep(1)
        for pic in self.pics:
            self.loadscreens = canvas.create_image(670, 384, image=pic)
            time.sleep(0.05)
            canvas.update()
            canvas.delete("all")

        time.sleep(1)
        self.pics=reversed(self.pics)
        for pic in self.pics:
            self.loadscreens = canvas.create_image(670, 384, image=pic)
            time.sleep(0.05)
            canvas.update()
            canvas.delete("all")

    def soundplayer(self, music):
        self.p = vlc.MediaPlayer(music)
        self.p.play()

    def start_new_game_button_clicked(self):
        self.start_button_int += 1
        return self.start_new_game()

    def back_button_clicked(self):
        self.back_button_int += 1
        return self.main_menu_buttons()

    def main_menu_buttons(self):
        self.item = canvas.create_image(683, 384, image=self.main_menu)
        self.start_new_game_button.place(relx=0.5, y=400, anchor=CENTER)
        self.load_saved_game_button.place(relx=0.5, y=500, anchor=CENTER)
        self.help_button.place(relx=0.5, y=600, anchor=CENTER)
        self.quit_button.place(relx=0.5, y=700, anchor=CENTER)

        self.house_atreides_button.place(x=222, rely=4, anchor=CENTER)
        self.house_ordos_button.place(x=694, rely=4, anchor=CENTER)
        self.house_harkonnen_button.place(x=1156, rely=4, anchor=CENTER)
        self.back_button.place(x=110, rely=4, anchor=CENTER)

    def house_button_clicked(self):
        self.game_int += 1
        return self.game()

    def start_new_game(self):
        if self.start_button_int > 0:
            canvas.delete("all")
            self.start_new_game_button.place(relx=0.5, y=4000, anchor=CENTER)
            self.load_saved_game_button.place(relx=0.5, y=4000, anchor=CENTER)
            self.help_button.place(relx=0.5, y=4000, anchor=CENTER)
            self.quit_button.place(relx=0.5, y=4000, anchor=CENTER)

            canvas.update()
            self.item1 = canvas.create_image(222, 300, image=self.house_atreides_pic)
            self.item2 = canvas.create_image(694, 300, image=self.house_ordos_pic)
            self.item3 = canvas.create_image(1156, 300, image=self.house_harkonnen_pic)

            self.house_atreides_button.place(x=222, rely=0.75, anchor=CENTER)
            self.house_ordos_button.place(x=694, rely=0.75, anchor=CENTER)
            self.house_harkonnen_button.place(x=1156, rely=0.75, anchor=CENTER)
            self.back_button.place(x=110, rely=0.92, anchor=CENTER)
            canvas.update()

    def game(self):
        if self.game_int > 0:
            canvas.delete("all")
            canvas.update()
            self.house_atreides_button.place(x=222, y=4000, anchor=CENTER)
            self.house_ordos_button.place(x=694, y=4000, anchor=CENTER)
            self.house_harkonnen_button.place(x=1156, y=4000, anchor=CENTER)
            self.back_button.place(x=110, y=4000, anchor=CENTER)

            self.item = canvas.create_image(683, 384, image=self.game_bg)

            self.level1_button.place(x=200, rely=0.2, anchor=CENTER)
            self.level2_button.place(x=300, rely=0.2, anchor=CENTER)
            self.level3_button.place(x=400, rely=0.2, anchor=CENTER)
            self.level4_button.place(x=500, rely=0.2, anchor=CENTER)
            self.level5_button.place(x=600, rely=0.2, anchor=CENTER)

            self.level6_button.place(x=200, rely=0.33, anchor=CENTER)
            self.level7_button.place(x=300, rely=0.33, anchor=CENTER)
            self.level8_button.place(x=400, rely=0.33, anchor=CENTER)
            self.level9_button.place(x=500, rely=0.33, anchor=CENTER)
            self.level10_button.place(x=600, rely=0.33, anchor=CENTER)

            self.level11_button.place(x=200, rely=0.46, anchor=CENTER)
            self.level12_button.place(x=300, rely=0.46, anchor=CENTER)
            self.level13_button.place(x=400, rely=0.46, anchor=CENTER)
            self.level14_button.place(x=500, rely=0.46, anchor=CENTER)
            self.level15_button.place(x=600, rely=0.46, anchor=CENTER)

            black_box = canvas.create_rectangle(810, 290, 1295, 610, fill="black", outline="grey", width=2)
            self.cti = canvas.create_image(900, 350, image=self.combat_tank_im)
            self.sti = canvas.create_image(900, 450, image=self.siege_tank_im)
            self.rli = canvas.create_image(900, 550, image=self.rocket_launcher_im)

            self.battle_button.place(x=1200, rely=0.92, anchor=CENTER)

    def battle_start(self):
        canvas.delete("all")
        canvas.update()

        self.level1_button.place(x=200, rely=4, anchor=CENTER)
        self.level2_button.place(x=300, rely=4, anchor=CENTER)
        self.level3_button.place(x=400, rely=4, anchor=CENTER)
        self.level4_button.place(x=500, rely=4, anchor=CENTER)
        self.level5_button.place(x=600, rely=4, anchor=CENTER)

        self.level6_button.place(x=200, rely=4, anchor=CENTER)
        self.level7_button.place(x=300, rely=4, anchor=CENTER)
        self.level8_button.place(x=400, rely=4, anchor=CENTER)
        self.level9_button.place(x=500, rely=4, anchor=CENTER)
        self.level10_button.place(x=600, rely=4, anchor=CENTER)

        self.level11_button.place(x=200, rely=4, anchor=CENTER)
        self.level12_button.place(x=300, rely=4, anchor=CENTER)
        self.level13_button.place(x=400, rely=4, anchor=CENTER)
        self.level14_button.place(x=500, rely=4, anchor=CENTER)
        self.level15_button.place(x=600, rely=4, anchor=CENTER)

        self.battle_button.place(x=1200, rely=4, anchor=CENTER)

        self.p.stop()

        self.battle_map_method()


    def battle_map_method(self):
        self.battle_bg = canvas.create_image(675, 400, image=self.battle_map)
        canvas.update()

        self.soundplayer(r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\battle.mp3")
        self.battle_start_counter = canvas.create_image(675, 400, image=self.battle_start3)
        canvas.update()
        time.sleep(1)
        canvas.delete(self.battle_start_counter)
        self.battle_start_counter = canvas.create_image(675, 400, image=self.battle_start2)
        canvas.update()
        time.sleep(1)
        canvas.update()
        canvas.delete(self.battle_start_counter)
        self.battle_start_counter = canvas.create_image(675, 400, image=self.battle_start1)
        canvas.update()
        time.sleep(1)
        canvas.update()
        canvas.delete(self.battle_start_counter)
        canvas.update()
        self.move()

    def move(self):
        x=0
        canvas.update()
        while x < 501:
            canvas.delete(self.tank1, self.tank2)
            self.tank1 = canvas.create_image(x+20, 350, image=self.atreides_combat_tank)
            self.tank2 = canvas.create_image(1326 - x, 350, image=self.atreides_combat_tank)
            x = x+3
            canvas.update()
            canvas.move(self.tank1, 3, 0)
            canvas.move(self.tank2, 3, 0)
            canvas.update()
            time.sleep(0.03)
            canvas.update()
        while self.enemy_health > 0:
            self.enemy_health-=2
            x=0
            if self.enemy_health == 10:
                time.sleep(0.1)
            else:
                time.sleep(1.5)
            canvas.update()
            while x < 290:
                canvas.delete(self.projectile)
                self.soundplayer(r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\tank_gun.mp3")
                self.projectile = canvas.create_image(x + 540, 350, image=self.projectile_img)
                x += 290/8
                canvas.update()
                canvas.move(self.projectile, 290/8, 0)
                time.sleep(0.03)
                canvas.update()
            canvas.lower(self.projectile)
            canvas.update()
        self.exp = canvas.create_image(826, 350, image=self.explosion1)
        time.sleep(0.05)
        canvas.update()
        canvas.delete(self.exp)
        self.exp = canvas.create_image(826, 350, image=self.explosion2)
        time.sleep(0.2)
        canvas.update()
        canvas.delete(self.tank2)
        canvas.update()
        canvas.delete(self.exp)
        canvas.update()
        time.sleep(0.2)
        self.mission_comp = canvas.create_image(675, 400, image=self.mission_complete)
        canvas.update()
        time.sleep(2)
        self.p.stop()









dune = Dune2_Blitz()
time.sleep(0.5)
#dune.loadscreen()
canvas.delete("all")
dune.soundplayer("C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\main_menu.mp3")
canvas.delete("all")
canvas.update()
time.sleep(1)
dune.main_menu_buttons()







root.mainloop()
