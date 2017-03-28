#dictionary

pirate = {"name": "Jack", "gold": 7, "has_wooden_leg": True}

#print(pirate["name"])

pirate["gold"] = 8

#print(pirate["gold"])

for key in pirate:
    print(key)

for key, value in pirate.items():
    print(key)
    print(value)

#for key in pirate:
#    print(key + ": " + str(pirate[key]))

#for key, value in pirate.items():
#    print(key + ": " + str(pirate[key]))
