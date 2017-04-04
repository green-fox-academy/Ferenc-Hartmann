class Garden():
    def __init__(self):
        self.flower_list = [["yellow", 0], ["blue", 0]]
        self.tree_list = [["purple", 0], ["orange", 0]]

    def printer(self):
        needed_water = 0
        for flowers in range(len(self.flower_list)):
            if self.flower_list[int(flowers)][1] < 5:
                print("The " + str(self.flower_list[int(flowers)][0]) + " flower " + "needs water.")
            if self.flower_list[int(flowers)][1] >= 5:
                print("The " + str(self.flower_list[int(flowers)][0]) + " flower " + "doesnt need water.")
        for trees in range(len(self.tree_list)):
            if self.tree_list[int(trees)][1] < 5:
                print("The " + str(self.tree_list[int(trees)][0]) + " tree " + "needs water.")
            if self.tree_list[int(trees)][1] >= 5:
                print("The " + str(self.tree_list[int(trees)][0]) + " tree " + "doesnt need water.")
        print()
    def add_flower(self, flower, water_volume=0):
        self.flower_list.append(flower, water_volume)

    def add_tree(self, tree, water_volume=0):
        self.tree_list.append(tree, water_volume)

    def watering(self, water_volume=0):
        self.water_volume = water_volume
        print("Watering with " + str(self.water_volume))
        needed_water = 0
        for flowers in range(len(self.flower_list)):
            if self.flower_list[int(flowers)][1] < 5:
                needed_water += 1
        for trees in range(len(self.tree_list)):
            if self.tree_list[int(trees)][1] < 10:
                needed_water +=1
        for flowers in range(len(self.flower_list)):
            if self.flower_list[int(flowers)][1] < 5:
                self.flower_list[int(flowers)][1] += (int(self.water_volume) / int(needed_water)) * 0.75
        for trees in range(len(self.tree_list)):
            if self.tree_list[int(trees)][1] < 10:
                self.tree_list[int(trees)][1] += (int(self.water_volume) / int(needed_water)) * 0.4
supergarden = Garden()
supergarden.printer()
supergarden.watering(40)
supergarden.printer()
supergarden.watering(70)
supergarden.printer()
