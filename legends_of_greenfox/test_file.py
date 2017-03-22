import random
health = 10
damage = 2
dex = 8
dragon_health = 10
dragon_damage = 1
dragon_dex = 10
a1 = 0
a2 = 0
a3 = 0
anykey = str(0)

while True:
    r = random.randrange(2, 12)
    print(r)
    if (dex + r) > (dragon_dex + r):
        dragon_health -= damage
        print("dragon took" + str(damage) + "damage")
    if (dex + r) < (dragon_dex + r):
        health -= dragon_damage
        print("You took" + str(dragon_damage) + "damage")
    else:
        print("You attacked very hard but no damage")
    if health == 0:
        print("health 0")
        break
    if dragon_health == 0:
        print("dragon_health 0")
        break
