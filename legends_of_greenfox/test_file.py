health = 0
damage = 0
dex = 0
a1 = 0
a2 = 0
a3 = 0
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
                        elif str(a3) == "r" or str(a3) == "R":
                            print("run")
                            raise SystemExit
                        elif str(a3) == "q" or str(a3) == "Q":
                            raise SystemExit
                            print("quit3")
                        else:
                            print("Please press [S] or [A]")

                elif str(a2) == "k" or str(a2) == "K":
                    print("knight")
                    anykey = str(input("anykey"))
                    print("prologue knight")
                    #Archer story starts here
                    a3 = input("a3")
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
