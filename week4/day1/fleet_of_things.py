#You have the Thing class
#You have the Fleet class
#You have the fleet_of_things.py file
#Download those, use those
#In the fleet_of_things file create a fleet
#Achieve this output:
#1. [ ] Get milk
#2. [ ] Remove the obstacles
#3. [x] Stand up
#4. [x] Eat lunch

class Fleet:
    def __init__(self):
        self.things = []

    def add(self, thing):
        self.things.append(thing)

    def __str__(self):
        result = ""
        for i in range(0, len(self.things)):
            result += str(i+1) + ". " + self.things[i].__str__() + "\n"
        return result

class Thing:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        return ("[x] " if self.completed else "[ ] ") + self.name



fleet = Fleet()
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

thing1 = Thing("Get milk")
fleet.add(thing1)

thing2 = Thing("Remove the obstacles")
fleet.add(thing2)

thing3 = Thing("Stand up")
thing3.complete()
fleet.add(thing3)

thing4 = Thing("Eat lunch")
thing4.complete()
fleet.add(thing4)
print(fleet)
