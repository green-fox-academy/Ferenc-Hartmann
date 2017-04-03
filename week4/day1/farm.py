#Reuse your Animal class
#Create a Farm class
#it has list of Animals
#it has slots which defines the number of free places for animals
#breed() -> creates a new animal if there's place for it
#slaughter() -> removes the least hungry animal

class Animal:
    hunger = 50
    thirst = 50

    def eat(self):
        self.hunger -= 1

    def drink(self):
        self.thirst -= 1

    def play(self):
        self.hunger += 1
        self.thirst += 1


class Farm():
    def __init__(self):
        self.list = []

    def breed(self, animal):
        if len(self.list) < 10:
            self.list.append([animal.hunger, animal.thirst])
        return self.list

    def slaughter(self):
        hungermeterrounds = 0
        survivercount = 0
        t = 0
        hungermeter = 100
        templist = []
        halfdeads = []
        for i in self.list:
            if self.list[int(hungermeterrounds)][0] < hungermeter:
                hungermeter = self.list[int(hungermeterrounds)][0]
            hungermeterrounds += 1
        for i in self.list:
            if self.list[int(survivercount)][0] != hungermeter:
                templist.append([self.list[int(survivercount)][0], self.list[int(survivercount)][1]])
            if self.list[int(survivercount)][0] == hungermeter:
                halfdeads.append([self.list[int(survivercount)][0], self.list[int(survivercount)][1]])
            if len(halfdeads) > 1 and t < 1:
                templist.append(halfdeads[0])
                t += 1
            survivercount += 1
        self.list = templist
        return self.list

poni = Animal()
poni.eat()
teve =Animal()
teve.eat()
poo = Animal()
ladyba = Animal()
dratini = Animal()
vigara = Animal()
tiger = Animal()
lista = Farm()

lista.breed(tiger)
lista.breed(vigara)
lista.breed(dratini)
lista.breed(ladyba)
lista.breed(poo)
lista.breed(teve)
lista.breed(poni)

lista.slaughter()
print(lista.list)
