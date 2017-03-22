import random
health = 0
damage = 0
dex = 0
dragon_health = 10
dragon_damage = 1
dragon_dex = 10
a1 = 0
a2 = 0
a3 = 0
anykey = str(0)

def battle_calculation(dragon):
    while True
        a = random.randrange(2, 12)
        print(a)






while True:
    #Main Menu
    a1 = input("a1")
    if str(a1) == "s" or str(a1) == "S":
        print("start")
        while True:
            #Character choosing
            a2 = input("a2")
            if str(a2) == "a" or str(a2) == "A":
                print("archer")
                health = 10
                damage = 2
                dex = 12
                anykey = str(input("press [Enter]"))
                print("prologue archer")
                while True:
                    #Archer story starts here
                    a3 = input("a3")
                    if str(a3) == "a" or str(a3) == "A":
                        print("Battle")
                        anykey = str(input("press [Enter]"))
# Battle calculation needs to be here!
                    elif str(a3) == "r" or str(a3) == "R":
                        print("game over")
                        raise SystemExit
                    elif str(a3) == "q" or str(a3) == "Q":
                        raise SystemExit
                        print("quit3")
                    else:
                        print("Please press [A] or [R]")
            if str(a2) == "k" or str(a2) == "K":
                print("knight")
                health = 20
                damage = 2
                dex = 8
                anykey = str(input("press [Enter]"))
                print("prologue knight")
                while True:
                    #Knight story starts here
                    a3 = input("a3")
                    if str(a3) == "a" or str(a3) == "A":
                        print("Battle")
                        anykey = str(input("press [Enter]"))
# Battle calculation needs to be here!
                    elif str(a3) == "r" or str(a3) == "R":
                        print("game over")
                        raise SystemExit
                    elif str(a3) == "q" or str(a3) == "Q":
                        raise SystemExit
                        print("quit3")
                    else:
                        print("Please press [A] or [R]")
    elif str(a1) == "h" or str(a1) == "H":
        print("help")
    elif str(a1) == "q" or str(a1) == "Q":
        raise SystemExit
        print("quit")
    elif str(a1) == "m" or str(a1) == "M":
        print("main")
    else:
        print("Please press [Q] or [S] or [H]")

#http://www.chris.com/ascii/joan/www.geocities.com/SoHo/7373/mythical2.html
#http://patorjk.com/software/taag/#p=display&h=1&f=Big&t=Help%20Menu
#http://loveascii.com/princess.html
