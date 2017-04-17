class Aircraft():
    def __init__(self, airplane):
#        self.F16 = [0, 0, 0, 0]
#        self.F35 = [0, 0, 0, 0]
        if airplane == "F16":
            self.F16 = ["F16", 8, 0, 30]    #[type, max_ammo, stored_ammo, basedamage]
            return self.F16
        if airplane == "F35":
            self.F35 = ["F35", 12, 0, 50]
            return self.F35
    def fight(self):
        damagef16 = self.F16[2] * self.F16[3]
        damagef35 = self.F35[2] * self.F35[3]
        if self.F16[0] == "F16":
            self.F16[2] = 0
            return damagef16
        if self.F35[0] == "F35":
            self.F35[2] = 0
            return damagef35

    def refill(self, number):
        if self.F16[0] == "F16":
            ammorefillf16 = (self.F16[1] - self.F16[2])
            if number > ammorefillf16:
                return number - ammorefillf16
            if ammorefillf16 > number:
                return 0
        if self.F35[0] == "F35":
            ammorefillf35 = (self.F35[1] - self.F35[2])
            if number > ammorefillf35:
                return number - ammorefillf35
            if ammorefillf35 > number:
                return 0

    def get_type(self):
        if self.F16[0] == "F16":
            return self.F16[0]
        if self.F35[0] == "F35":
            return self.F35[0]

    def get_status(self):
        if self.F16[0] == "F16":
            return ("Type " + str(self.F16[0]) + ", Ammo: " + str(self.F16[2]) + " Base Damage: " + str(self.F16[3]) + ", All damage: " + str((self.F16[2] * self.F16[3])))
        if self.F35[0] == "F35":
            return ("Type " + str(self.F35[0]) + ", Ammo: " + str(self.F35[2]) + " Base Damage: " + str(self.F35[3]) + ", All damage: " + str((self.F35[2] * self.F35[3])))

class Carrier():
    def __init__(self, maxammo, ammo, health):
        self.maxammo = maxammo
        self.ammo = ammo
        self.health = health
        self.plane = []

    def add_aircraft(self, airplane):
        if airplane == "F16":
            self.plane.append(Aircraft.__init__(self, airplane))
        if airplane == "F35":
            self.plane.append(Aircraft.__init__(self, airplane))

    def fill(self):
        self.counter = 0
        for i in range(len(self.plane)):
            Aircraft.refill(self, self.plane[int(i)])

#sky = Aircraft("F16")
#skynet = Aircraft("F35")
#print(sky.get_status())
#print(skynet.get_status())

water = Carrier(1000, 1000, 5000)
water.add_aircraft("F35")
water.add_aircraft("F35")
water.add_aircraft("F35")
water.add_aircraft("F16")
water.add_aircraft("F16")

print(water.plane)
#print(sky.get_status())
