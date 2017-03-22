hp = 0
damage = 0
dex = 0
a1 = 0
a2 = 0
anykey = str(0)
def first_decision():
    while True:
#Main Menu
        a1 = input("a1")
        if str(a1) == "s" or str(a1) == "S":
            print("start")
            while True:
#Character choosing
                a2 = input("a2")
                if str(a2) == "a" or str(a1) == "A":
                    print("archer")
                    anykey = str(input("anykey"))
                    print("prologue archer")
                elif str(a2) == "k" or str(a2) == "K":
                    print("knight")
                    anykey = str(input("anykey"))
                    print("prologue knight")
                elif str(a2) == "q" or str(a2) == "Q":
                    raise SystemExit
                    print("quit2")
                else:
                    print("Please press [A] or [K]")


        elif str(a1) == "h" or str(a1) == "H":
            print("help")
        elif str(a1) == "q" or str(a1) == "Q":
            raise SystemExit
            print("quit")
        elif str(a1) == "m" or str(a1) == "M":
            print("main")
        else:
            print("Please press [Q] or [S] or [H]")
first_decision()
