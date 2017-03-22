def black_screen():
    print("black_screen")
black_screen()


def main_screen():
    print("main_screen")
main_screen()


a1 = input("")


while str(a1) == "q" or str(a1) == "Q" or str(a1) == "h" or str(a1) == "H" or str(a1) == "s" or str(a1) == "S":
    print("Please [Q] or [S] or [H]")

def help_screen():
    if str(a1) == "h" or str(a1) == "H":
        print("help_screen")
help_screen()


a2 = input("")


if str(a2) == "m" or str(a2) == "M":
    main_screen()


a1 = input("")


def quit_screen():
    if str(a1) == "q" or str(a1) == "Q":
        print("")
quit_screen()


if str(a1) == "s" or str(a1) == "S":
    print("s pressed")




#http://www.chris.com/ascii/joan/www.geocities.com/SoHo/7373/mythical2.html
#http://patorjk.com/software/taag/#p=display&h=1&f=Big&t=Help%20Menu
#http://loveascii.com/princess.html
