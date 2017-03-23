# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts listOfNumbers as an input
# it should return "true" if it contains all, otherwise print "false"

listOfNumbers = [2, 4, 6, 8, 10, 12, 14, 16]


def container(n):
    s = 0
    if (n) in listOfNumbers:
        s += 1
    if (2 * n) in listOfNumbers:
        s += 1
    if (3 * n) in listOfNumbers:
        s += 1
    if (4 * n) in listOfNumbers:
        s += 1
    if s == 4:
        return True
    else:
        return False

print(container(4))
