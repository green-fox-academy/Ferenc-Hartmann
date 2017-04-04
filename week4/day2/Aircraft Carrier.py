class Aircraft():
    def __init__(self):
        self.F16 = ["F16", 8, 0, 30]
        self.F35 = ["F35", 12, 0, 50]
    def fight(self):
        damagef16 = (self.F16[1] - self.F16[2]) * self.F16[3]
        damagef35 = (self.F35[1] - self.F35[2]) * self.F16[3]
        if self.F16[0] = "F16":
            return damagef16
        if self.F35[0] = "F35":
            return damagef35

    def refill(self, number):
        if self.F16[0] = "F16":
            ammorefillf16 = (self.F16[1] - self.F16[2])
            if number > ammorefillf16:
                return (number - ammorefillf16)
            if ammorefillf16 > number:
                return 0
        if self.F35[0] = "F35":
            ammorefillf35 = (self.F35[1] - self.F35[2])
            if number > ammorefillf35:
                return (number - ammorefillf35)
            if ammorefillf35 > number:
                return 0

    def get_type(self):
        if self.F16[0] = "F16":
            return self.F16[0]
        if self.F35[0] = "F35":
            return self.F35[0]

    def get_status(self):
        if self.F16[0] = "F16":
            return ("Type " + str(self.F16[0]) + ", Ammo: " + str(self.F16[2]) + " Base Damage: " + str(self.F16[3]) + ", " + str((self.F16[2] * self.F16[3]))
        if self.F35[0] = "F35":
            return ("Type " + str(self.F35[0]) + ", Ammo: " + str(self.F35[2]) + " Base Damage: " + str(self.F35[3]) + ", All damage: " + str((self.F35[2] * self.F35[3]))
