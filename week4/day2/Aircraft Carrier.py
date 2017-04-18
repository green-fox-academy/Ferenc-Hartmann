class Aircraft():
    def __init__(self, airplane):
        self.plane_data_list = [airplane, 8, 0, 30]
#        if airplane == "F16":
#            self.F16 = ["F16", 8, 0, 30]    #[type, max_ammo, stored_ammo, basedamage]
#            return self.F16
#        if airplane == "F35":
#            self.F35 = ["F35", 12, 0, 50]
#            return self.F35
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

    def get_status(self, plane_type, stored_ammo, base_damage):
        return ("Type " + str(plane_type) + ", Ammo: " + str(stored_ammo) + " Base Damage: " + str(base_damage) + ", All damage: " + str((stored_ammo * base_damage)))

class Carrier():
    def __init__(self, maxammo, ammo, health):
        self.maxammo = maxammo
        self.ammo = ammo
        self.health = health
        self.plane = []

    def add_aircraft(self, airplane):
        #if airplane == "F16":
            #self.plane.append(Aircraft.__init__(self, airplane))
        self.plane.append(Aircraft(airplane).plane_data_list)
        #if airplane == "F35":
            #self.plane.append(Aircraft.__init__(self, airplane))
        #    self.plane.append(Aircraft("F35"))
        #print(self.plane)
    def fill(self):
        if self.ammo > 0:
            sorted_planes = sorted(self.plane)
            self.plane = sorted_planes[::-1]
            for i in range(len(self.plane)):
                return_list = Aircraft.refill(self, self.plane[int(i)][1], self.plane[int(i)][2], self.ammo)
                self.plane[int(i)][2] = return_list[0]
                self.ammo = return_list[1]
        if self.ammo == 0:
            print("No ammo in carrier.")

    def fight(self, health):
        self.enemy_health = health
        total_damage = 0
        for i in range(len(self.plane)):
            total_damage += self.plane[int(i)][2] * self.plane[int(i)][3]
            self.plane[int(i)][2] = 0
        self.enemy_health -= total_damage
        if self.enemy_health <= 0:
            print("It's dead Jim :(")

    def get_status(self):
        total_damage2 = 0
        for i in range(len(self.plane)):
            total_damage2 += self.plane[int(i)][2] * self.plane[int(i)][3]
        print("Aircraft count: " + str(len(self.plane)) + ", Ammo Storage: " + str(self.ammo) + ", Total damage: " + str(total_damage2))
        print("Aircrafts:")
        for i in range(len(self.plane)):
            print(Aircraft.get_status(self, self.plane[int(i)][0], self.plane[int(i)][2], self.plane[int(i)][3]))

water = Carrier(2000, 2000, 5000)
water.add_aircraft("F35")
water.add_aircraft("F16")
water.add_aircraft("F16")
water.add_aircraft("F35")
water.add_aircraft("F35")

water.get_status()
water.fill()
water.get_status()

water.fight(5000)
water.get_status()
water.fill()
water.get_status()
#print(water.plane)
#water.fill()
#water.fight(720)
#print(water.enemy_health)
#print(water.ammo)
