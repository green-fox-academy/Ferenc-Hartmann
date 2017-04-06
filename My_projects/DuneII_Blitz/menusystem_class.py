#DuneII Blitz created by Ferenc Hartmann
import time
from tkinter import*
root = Tk()
root.attributes('-fullscreen', True)
canvas = Canvas(root, width='1366', height='768', bg='black')
canvas.pack()
canvas.update()

class Dune2_blitz():
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

        self.loadscreens = 0
        self.start_button_int = 0
        self.back_button_int = 0
        self.game_int = 0

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

    def soundplayer(self):
        import vlc
        p = vlc.MediaPlayer("C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\main_menu.mp3")
        p.play()

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
        print(self.self.start_button_int)

    def game(self):
        if self.game_int > 0:
            canvas.delete("all")
            canvas.update()
            self.house_atreides_button.place(x=222, y=4000, anchor=CENTER)
            self.house_ordos_button.place(x=694, y=4000, anchor=CENTER)
            self.house_harkonnen_button.place(x=1156, y=4000, anchor=CENTER)
            self.back_button.place(x=110, y=4000, anchor=CENTER)
        print(self.game_int)




dune = Dune2_blitz()
time.sleep(0.5)
dune.loadscreen()
canvas.delete("all")
dune.soundplayer()
canvas.delete("all")
canvas.update()
time.sleep(1)
dune.main_menu_buttons()
root.mainloop()
