#Legends of Greenfox: Made by Ferenc Hartmann from Greenfox Academy

import random
import time
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
battle_rounds = 0

#Interactive program starts here
while True:
    #Main Menu
    user_input_lvl1 = input("")
    if str(user_input_lvl1) == "s" or str(user_input_lvl1) == "S":
        print("character choosing screen")
        while True:
            character_choose_screen()
            user_input_lvl2 = input("")
            #Choosing archer
            if str(user_input_lvl2) == "a" or str(user_input_lvl2) == "A":
                archer_chosen()
                health = 10
                damage = 2
                dex = 12
                anykey = str(input(""))
                prologue()
                while True:
                    #Archer story starts here
                    user_input_lvl3 = input("")
                    if str(user_input_lvl3) == "a" or str(user_input_lvl3) == "A":
                        dragon_attacks()
                        anykey = str(input(""))
                        black_screen()
                        #Battle calculation
                        while health > 0 and dragon_health > 0:
                            time.sleep(1)
                            battle_rounds += 1
                            ua = dex + random.randrange(2, 12)
                            da = dragon_dex + random.randrange(2, 12)
                            if ua > da:
                                dragon_health = (dragon_health - damage)
                                print("                                                                       ---------------ROUND " + str(battle_rounds) + "---------------")
                                print("")
                                print("                                                                                DRAGON TOOK " + str(damage) + " DAMAGE")
                                print("                                                        YOUR HEALTH: " + str(health) +           "                                     DRAGON'S HEALTH: " + str(dragon_health) + "  ")
                                print("")
                                if dragon_health == 0:
                                    anykey = str(input(""))
                                    wingame()
                                    anykey = str(input(""))
                                    quit_screen()
                                    raise SystemExit
                            elif ua < da:
                                health =  (health - dragon_damage)
                                print("                                                                       ---------------ROUND " + str(battle_rounds) + "---------------")
                                print("")
                                print("                                                                                 YOU TOOK " + str(dragon_damage) + " DAMAGE")
                                print("                                                        YOUR HEALTH: " + str(health) +           "                                     DRAGON'S HEALTH: " + str(dragon_health) + "  ")
                                print("")

                                if health == 0:
                                    anykey = str(input(""))
                                    losegame()
                                    anykey = str(input(""))
                                    quit_screen()
                                    raise SystemExit
                            elif ua == da:
                                print("                                                                       ---------------ROUND " + str(battle_rounds) + "---------------")
                                print("")
                                print("                                                                         YOU ATTACK VERY HARD BUT NO DAMAGE")
                                print("")
                    elif str(user_input_lvl3) == "r" or str(user_input_lvl3) == "R":
                        runlosegame()
                        anykey = str(input(""))
                        quit_screen()
                        raise SystemExit
                    elif str(user_input_lvl3) == "q" or str(user_input_lvl3) == "Q":
                        quit_screen()
                        raise SystemExit
                    else:
                        print("Please press [A] or [R]")
            #Choosing knight
            if str(user_input_lvl2) == "k" or str(user_input_lvl2) == "K":
                knight_chosen()
                health = 20
                damage = 2
                dex = 8
                anykey = str(input(""))
                prologue()
                while True:
                    #Knight story starts here
                    user_input_lvl3 = input("")
                    if str(user_input_lvl3) == "a" or str(user_input_lvl3) == "A":
                        dragon_attacks()
                        anykey = str(input(""))
                        black_screen()
                        #Battle calculation
                        while health > 0 and dragon_health > 0:
                            time.sleep(0.5)
                            battle_rounds += 1
                            ua = dex + random.randrange(2, 12)
                            da = dragon_dex + random.randrange(2, 12)
                            if ua > da:
                                dragon_health = (dragon_health - damage)
                                print("                                                                       ---------------ROUND " + str(battle_rounds) + "---------------")
                                print("")
                                print("                                                                                DRAGON TOOK " + str(damage) + " DAMAGE")
                                print("                                                        YOUR HEALTH: " + str(health) +           "                                     DRAGON'S HEALTH: " + str(dragon_health) + "  ")
                                print("")
                                if dragon_health == 0:
                                    anykey = str(input(""))
                                    wingame()
                                    anykey = str(input(""))
                                    quit_screen()
                                    raise SystemExit
                            elif ua < da:
                                health =  (health - dragon_damage)
                                print("                                                                       ---------------ROUND " + str(battle_rounds) + "---------------")
                                print("")
                                print("                                                                                 YOU TOOK " + str(dragon_damage) + " DAMAGE")
                                print("                                                        YOUR HEALTH: " + str(health) +           "                                     DRAGON'S HEALTH: " + str(dragon_health) + "  ")
                                print("")

                                if health == 0:
                                    anykey = str(input(""))
                                    losegame()
                                    anykey = str(input(""))
                                    quit_screen()
                                    raise SystemExit
                            elif ua == da:
                                print("                                                                       ---------------ROUND " + str(battle_rounds) + "---------------")
                                print("")
                                print("                                                                         YOU ATTACK VERY HARD BUT NO DAMAGE")
                                print("")
                    elif str(user_input_lvl3) == "r" or str(user_input_lvl3) == "R":
                        runlosegame()
                        anykey = str(input(""))
                        quit_screen()
                        raise SystemExit
                    elif str(user_input_lvl3) == "q" or str(user_input_lvl3) == "Q":
                        quit_screen()
                        raise SystemExit
                    else:
                        print("Please press [A] or [R]")
            elif str(user_input_lvl2) == "q" or str(user_input_lvl2) == "Q":
                quit_screen()
                raise SystemExit
            else:
                print("Please press [A] or [K]")
    elif str(user_input_lvl1) == "h" or str(user_input_lvl1) == "H":
        help_screen()
    elif str(user_input_lvl1) == "q" or str(user_input_lvl1) == "Q":
        quit_screen()
        raise SystemExit
    elif str(user_input_lvl1) == "m" or str(user_input_lvl1) == "M":
        main_screen()
    else:
        print("Please press [Q] or [S] or [H]")

#http://www.chris.com/ascii/joan/www.geocities.com/SoHo/7373/mythical2.html
#http://patorjk.com/software/taag/#p=display&h=1&f=Big&t=Help%20Menu
#http://loveascii.com/princess.html
