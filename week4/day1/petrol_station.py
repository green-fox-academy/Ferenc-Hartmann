#Create Station and Car classes
#Station
#gas_amount
#refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount
#Car
#gas_amount
#capacity
#create constructor for Car where:
#initialize gas_amount -> 0
#initialize capacity -> 100

class Station:
    gas_amount = 10000
    def refill(self, car):
        self.gas_amount -= car.capacity
        car.gasamount = car.capacity

class Car:
    def __init__(self):
        self.gasamount = 0
        self.capacity = 100

castrol = Station()
lada = Car()
print(lada.gasamount)
castrol.refill(lada)
print(lada.gasamount)
