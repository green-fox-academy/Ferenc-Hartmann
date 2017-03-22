
# - Create an array variable named `ag`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Double all the values in the array

x = 0
ag = [3, 4, 5, 6, 7]

while x < len(ag):
    ag[x] *= 2
    x += 1
print(ag)
