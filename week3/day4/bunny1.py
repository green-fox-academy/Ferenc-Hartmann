# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

number = int(input("Please enter the number of bunnies to sum their ears :" ))

def bunnyears(n):
    ear = 0
    if n == 1: #base case
        ear += 2
        return ear
    else:
        return ((ear+2) + (bunnyears(n-1)))

bunnyears(number)
print(bunnyears(number))
