import random
health = 20
damage = 4
dex = 8
dragon_health = 20
dragon_damage = 2
dragon_dex = 8
a1 = 0
a2 = 0
a3 = 0
anykey = str(0)

while health > 0 and dragon_health > 0:
    ua = dex + random.randrange(2, 12)
    da = dragon_dex + random.randrange(2, 12)
    if ua > da:
        dragon_health = (dragon_health - damage)
        print("dragon took " + str(damage) + " damage")
        print("")
        if dragon_health == 0:
            print("dragon_health 0")
    elif ua < da:
        health =  (health - dragon_damage)
        print("You took " + str(dragon_damage) + " damage")
        print("")
        if health == 0:
            print("health 0")
    elif ua == da:
        print("You attacked very hard but no damage")
        print(ua, da)
