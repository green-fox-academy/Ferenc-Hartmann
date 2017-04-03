class Sharpie:
    color = ""
    width = ""
    ink_amount = 100
    def use(self, a):
        self.ink_amount -= a
        return self.ink_amount

poni = Sharpie()
poni.color = "pink"
poni.width = 4.9

print(poni.color, poni.width)
poni.use(10)
print(poni.ink_amount)
