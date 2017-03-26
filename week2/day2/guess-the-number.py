# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

import random

a = random.randrange(1, 10)

user_input_1 = input("I calculated and stored a number between 1 and 10. Please guess it!")

while user_input_1 != a:
    if int(user_input_1) < a:
        user_input_1 = input("The stored number is higher than your typed number. Please gueass again!")
        print("")
    elif int(user_input_1) > a:
        user_input_1 = input("The stored number is lower than your typed number. Please gueass again!")
        print("")
    elif int(user_input_1) == a:
        print("You found the number: " + str(a))
        break
