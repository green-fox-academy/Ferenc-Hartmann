#DuneII Blitz created by Ferenc Hartmann
import time
from tkinter import*
root = Tk()
root.attributes('-fullscreen', True)
canvas = Canvas(root, width='1366', height='768', bg='black')
canvas.pack()
canvas.update()


def loadscreen():
    a = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart10.png")
    b = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart9.png")
    c = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart8.png")
    d = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart7.png")
    e = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart6.png")
    f = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart5.png")
    g = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart4.png")
    h = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart3.png")
    i = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart2.png")
    j = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\hart1.png")
    pics=[a,b,c,d,e,f,g,h,i,j]

    time.sleep(1)

    for pic in pics:
        loadscreen = canvas.create_image(670, 384, image=pic)
        time.sleep(0.05)
        canvas.update()
        canvas.delete("all")

    time.sleep(1)
    pics=reversed(pics)

    for pic in pics:
        loadscreen = canvas.create_image(670, 384, image=pic)
        time.sleep(0.05)
        canvas.update()
        canvas.delete("all")

loadscreen()
canvas.delete("all")
canvas.update()
time.sleep(1)


def soundplayer():
    import vlc
    p = vlc.MediaPlayer("C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\main_menu.mp3")
    p.play()

soundplayer()
time.sleep(1)

def start_new_game_button_clicked():
    global start_button
    start_button = 0
    start_button += 1
    return start_new_game()

def back_button_clicked():
    global back_button
    back_button = 0
    back_button += 1
    return main_menu_buttons()

main_menu = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune1pro.png")

start_new_game_button = Button(width=20, height=1, fg="white", bg="black", text="Start New Game", font=("Harrington",30,"bold"), command = start_new_game_button_clicked)
load_saved_game_button = Button(width=20, height=1, fg="white", bg="black", text="Load Saved Game", font=("Harrington",30,"bold"))
help_button = Button(width=20, height=1, fg="white", bg="black", text="Help", font=("Harrington",30,"bold"))
quit_button = Button(width=20, height=1, fg="white", bg="black", text="Quit", font=("Harrington",30,"bold"), command = root.quit)

house_atreides_button = Button(width=15, height=1, fg="blue", bg="black", text="House Atreides", font=("Harrington",30,"bold"))
house_ordos_button = Button(width=15, height=1, fg="green", bg="black", text="House Ordos", font=("Harrington",30,"bold"))
house_harkonnen_button = Button(width=15, height=1, fg="red", bg="black", text="House Harkonnen", font=("Harrington",30,"bold"))
back_button = Button(width=5, height=1, fg="white", bg="black", text="Back", font=("Harrington",30,"bold"), command=back_button_clicked)


def main_menu_buttons():
    item = canvas.create_image(683, 384, image=main_menu)
    start_new_game_button.place(relx=0.5, y=400, anchor=CENTER)
    load_saved_game_button.place(relx=0.5, y=500, anchor=CENTER)
    help_button.place(relx=0.5, y=600, anchor=CENTER)
    quit_button.place(relx=0.5, y=700, anchor=CENTER)

    house_atreides_button.place(x=222, rely=4, anchor=CENTER)
    house_ordos_button.place(x=694, rely=4, anchor=CENTER)
    house_harkonnen_button.place(x=1156, rely=4, anchor=CENTER)
    back_button.place(x=110, rely=4, anchor=CENTER)

house_atreides_pic = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\houseatreides.png")
house_ordos_pic = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\houseordos.png")
house_harkonnen_pic = PhotoImage(file=r"C:\Greenfox\Ferenc-Hartmann\My_projects\DuneII_Blitz\dune2\househarkonnen.png")

def start_new_game():
    if start_button > 0:
        canvas.delete("all")
        start_new_game_button.place(relx=0.5, y=4000, anchor=CENTER)
        load_saved_game_button.place(relx=0.5, y=4000, anchor=CENTER)
        help_button.place(relx=0.5, y=4000, anchor=CENTER)
        quit_button.place(relx=0.5, y=4000, anchor=CENTER)

        canvas.update()
        item1 = canvas.create_image(222, 300, image=house_atreides_pic)
        item2 = canvas.create_image(694, 300, image=house_ordos_pic)
        item3 = canvas.create_image(1156, 300, image=house_harkonnen_pic)

        house_atreides_button.place(x=222, rely=0.75, anchor=CENTER)
        house_ordos_button.place(x=694, rely=0.75, anchor=CENTER)
        house_harkonnen_button.place(x=1156, rely=0.75, anchor=CENTER)
        back_button.place(x=110, rely=0.92, anchor=CENTER)
        canvas.update()

        canvas.update()



main_menu_buttons()




root.mainloop()
