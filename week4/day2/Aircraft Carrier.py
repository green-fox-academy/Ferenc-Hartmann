class Aircraft():
    def __init__(self, airplane):
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

    def refill(self, max_ammo, stored_ammo, number):
            ammorefill = (max_ammo - stored_ammo)
            if number > ammorefill:
                return [ammorefill, number - ammorefill]
            if ammorefill > number:
                return [number, 0]

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
        sorted_planes = sorted(self.plane)
        self.plane = sorted_planes[::-1]
        for i in range(len(self.plane)):
            return_list = Aircraft.refill(self, self.plane[int(i)][1], self.plane[int(i)][2], self.ammo)
            self.plane[int(i)][2] = return_list[0]
            self.ammo = return_list[1]

water = Carrier(1000, 30, 5000)
water.add_aircraft("F35")
water.add_aircraft("F16")
water.add_aircraft("F16")
water.add_aircraft("F35")
water.add_aircraft("F35")



water.fill()
print(water.plane)
