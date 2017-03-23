import random
health = 0
damage = 0
dex = 0
dragon_health = 10
dragon_damage = 1
dragon_dex = 10
user_input_lvl1 = 0
user_input_lvl2 = 0
user_input_lvl3 = 0
anykey = str(0)

while True:
    #Main Menu
    user_input_lvl1 = input("user_input_lvl1")
    if str(user_input_lvl1) == "s" or str(user_input_lvl1) == "S":
        print("character choosing screen")
        while True:
            user_input_lvl2 = input("user_input_lvl2")
            #Choosing archer
            if str(user_input_lvl2) == "a" or str(user_input_lvl2) == "A":
                print("archer chosen screen")
                health = 10
                damage = 2
                dex = 12
                anykey = str(input("press [Enter]"))
                print("archer prologue screen")
                while True:
                    #Archer story starts here
                    user_input_lvl3 = input("user_input_lvl3")
                    if str(user_input_lvl3) == "a" or str(user_input_lvl3) == "A":
                        print("archer pre-battle screen")
                        anykey = str(input("press [Enter]"))
                        #Battle calculation
                        while health > 0 and dragon_health > 0:
                            ua = dex + random.randrange(2, 12)
                            da = dragon_dex + random.randrange(2, 12)
                            if ua > da:
                                dragon_health = (dragon_health - damage)
                                print("dragon took " + str(damage) + " damage")
                                print("")
                                if dragon_health == 0:
                                    print("dragon_health 0 and you win!")
                            elif ua < da:
                                health =  (health - dragon_damage)
                                print("You took " + str(dragon_damage) + " damage")
                                print("")
                                if health == 0:
                                    print("health 0 and you died")
                            elif ua == da:
                                print("You attacked very hard but no damage")
                                print("")
                    elif str(user_input_lvl3) == "r" or str(user_input_lvl3) == "R":
                        print("game over")
                        raise SystemExit
                    elif str(user_input_lvl3) == "q" or str(user_input_lvl3) == "Q":
                        print("quit3")
                        raise SystemExit
                    else:
                        print("Please press [A] or [R]")
            #Choosing knight
            if str(user_input_lvl2) == "k" or str(user_input_lvl2) == "K":
                print("knight chosen screen")
                health = 20
                damage = 2
                dex = 8
                anykey = str(input("press [Enter]"))
                print("knight prologue screen")
                while True:
                    #Knight story starts here
                    user_input_lvl3 = input("user_input_lvl3")
                    if str(user_input_lvl3) == "a" or str(user_input_lvl3) == "A":
                        print("knight pre-battle screen")
                        anykey = str(input("press [Enter]"))
                        #Battle calculation
                        while health > 0 and dragon_health > 0:
                            ua = dex + random.randrange(2, 12)
                            da = dragon_dex + random.randrange(2, 12)
                            if ua > da:
                                dragon_health = (dragon_health - damage)
                                print("dragon took " + str(damage) + " damage")
                                print("")
                                if dragon_health == 0:
                                    print("dragon_health 0 and you win!")
                            elif ua < da:
                                health =  (health - dragon_damage)
                                print("You took " + str(dragon_damage) + " damage")
                                print("")
                                if health == 0:
                                    print("health 0 and you died")
                            elif ua == da:
                                print("You attacked very hard but no damage")
                                print("")
                    elif str(user_input_lvl3) == "r" or str(user_input_lvl3) == "R":
                        print("game over")
                        raise SystemExit
                    elif str(user_input_lvl3) == "q" or str(user_input_lvl3) == "Q":
                        print("quit3")
                        raise SystemExit
                    else:
                        print("Please press [A] or [R]")
            elif str(user_input_lvl2) == "q" or str(user_input_lvl2) == "Q":
                print("quit3")
                raise SystemExit
            else:
                print("Please press [A] or [K]")
    elif str(user_input_lvl1) == "h" or str(user_input_lvl1) == "H":
        print("help")
    elif str(user_input_lvl1) == "q" or str(user_input_lvl1) == "Q":
        print("quit")
        raise SystemExit
    elif str(user_input_lvl1) == "m" or str(user_input_lvl1) == "M":
        print("main")
    else:
        print("Please press [Q] or [S] or [H]")

#http://www.chris.com/ascii/joan/www.geocities.com/SoHo/7373/mythical2.html
#http://patorjk.com/software/taag/#p=display&h=1&f=Big&t=Help%20Menu
#http://loveascii.com/princess.html
