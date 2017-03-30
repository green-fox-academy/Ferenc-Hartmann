# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

number = int(input("Please enter the number of bunnies to sum their ears :" ))

def bunnyears(n):
    ear = 0
    if n == 1: #base case
        ear += 2
        return ear
    elif n % 2 == 0:
        return ((ear+3) + (bunnyears(n-1)))
    else:
        return ((ear+2) + (bunnyears(n-1)))

bunnyears(number)
print(bunnyears(number))
