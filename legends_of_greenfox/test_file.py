a1 = 0
def first_decision(x):
    while True:
        a1 = input("")
        if str(a1) == "q" or str(a1) == "Q":
            break
            print("quit")
        elif str(a1) == "h" or str(a1) == "H":
            print("help")
        elif str(a1) == "s" or str(a1) == "S":
            print("start")
        elif str(a1) == "m" or str(a1) == "M":
            print("main")
        else:
            print("Please press [Q] or [S] or [H]")
first_decision(x)
