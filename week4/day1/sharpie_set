#Sharpie Set

#Reuse your Sharpie class
#Create SharpieSet class
#it contains a list of Sharpie
#count_usable() -> sharpie is usable if it has ink in it
#remove_trash() -> removes all unusable sharpies

class Sharpie():
    def __init__(self, color="", width=0.0):
        self.color = color
        self.width = width
        self.ink_amount = 100
    def use(self, a):
        self.ink_amount -= a
        return self.ink_amount

class SharpieSet():
    def __init__(self):
        self.list = []

    def add(self, sharpie):
        self.list.append([sharpie.color, sharpie.width, sharpie.ink_amount])
        return self.list

    def count_usable(self):
        counter = 0
        n=0
        for i in self.list:
            if self.list[int(n)][2] != 0:
                counter += 1
            n+=1
        return counter

    def remove_trash(self):
        n=0
        templist = []
        for i in self.list:
            if self.list[int(n)][2] != 0:
                templist.append([self.list[int(n)][0], self.list[int(n)][1], self.list[int(n)][2]])
            n+=1
        self.list = templist

poni = Sharpie("pink", 4.9)
teve = Sharpie("brown", 7.6)
teve.use(100)
lista = SharpieSet()
lista.add(poni)
lista.add(teve)
lista.remove_trash()
print(lista.list)
print(lista.count_usable())
