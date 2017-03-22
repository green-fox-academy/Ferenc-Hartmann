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

def battle_calculation():
    while True:
        a = random.randrange(2, 12)
        if (dex + a) > (dragon_dex + a):
            dragon_health -= damage
            print("dragon took" + damage + "damage")
        if (dex + a) < (dragon_dex + a):
            health -= dragon_damage
            print("You took" + damage + "damage")
        if health == 0:
            break
            print("health 0")
        if dragon_health == 0:
            break
            print("dragon_health 0")
        else:
            print("You attacked very hard but no damage")
battle_calculation()
