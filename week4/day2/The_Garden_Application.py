class Garden():
    def __init__(self, water_volume=0):
        self.water_volume = water_volume
        self.flower_list = [["yellow", 0], ["blue", 0]]
        self.tree_list = [["purple", 0], ["orange", 0]]

    def printer(self):
        print("The " + str(self.flower_list[0][0]) + " flower " + "needs water.")

    def add_flower(self, flower, water_volume=0):
        self.flower_list.append(flower, water_volume)

    def add_tree(self, tree, water_volume=0):
        self.tree_list.append(tree, water_volume)

    def watering(self, water_volume=0):
        print("Watering with " + str(water_volume))
        needed_water = 0
        for flowers in range(len(self.flower_list)):
            if self.flower_list[int(flowers)][1] < 5:
                needed_water += 1
        for trees in range(len(self.tree_list)):
            if self.tree_list[int(trees)][1] < 10:
                needed_water +=1
        for flowers in range(len(self.flower_list)):
            if self.flower_list[int(flowers)][1] < 5:
                self.flower_list[int(flowers)][1] += (int(water_volume) / int(needed_water)) * 0.75
        for trees in range(len(self.tree_list)):
            if self.tree_list[int(trees)][1] < 10:
                self.tree_list[int(trees)][1] += (int(water_volume) / int(needed_water)) * 0.4

supergarden = Garden()
supergarden.printer()
supergarden.watering(40)
