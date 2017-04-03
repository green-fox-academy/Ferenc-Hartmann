#Create Sharpie class
#We should know about each sharpie their color (which should be a string), width (which will be a floating point number), ink_amount (another floating point number)
#When creating one, we need to specify the color and the width
#Every sharpie is created with a default 100 as ink_amount
#We can use() the sharpie objects
#which decreases inkAmount

class Sharpie():
    def __init__(self, color="", width=0.0):
        self.ink_amount = 100
        self.color = color
        self.width = width
    def use(self, a):
        self.ink_amount -= a
        return self.ink_amount

poni = Sharpie("pink", 4.9)
poni.use(10)
print(poni.color, poni.width, poni.ink_amount)
