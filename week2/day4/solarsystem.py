# Saturn is missing from the planetList
# Insert it into the correct position

planetlist = ["Mercury","Venus","Earth","Mars","Jupiter","Uranus","Neptune"]

planetlist = planetlist + ["Saturn"]

planetlist[7], planetlist[5] = planetlist[5], planetlist[7]
planetlist[7], planetlist[6] = planetlist[6], planetlist[7]
print(planetlist)
