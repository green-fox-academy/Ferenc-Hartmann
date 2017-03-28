#1XP
#
#Exercise
#
#Create a function named is anagram following your current language's style guide. It should take two strings and return a #boolean value depending on whether its an anagram or not.
#
#Examples
#
#   input 1	input 2	outut
#   "dog"	"god"	true
#   "green"	"fox"	false

import random

user_input_0 = input("I will start the calculation from 1. Please enter which should be the highest number what I will calculate for you.")
print("")
user_input_1 = input("I have calculated a number between 1 and " + user_input_0 + ". You have 5 lives. Please guess it!")

a = random.randrange(1, int(user_input_0))
lives = 5

while lives > 0:
    lives -= 1
    if int(user_input_1) < a:
        user_input_1 = input("The stored number is higher than your typed number. Please gueass again!")
        print("")
    elif int(user_input_1) > a:
        user_input_1 = input("The stored number is lower than your typed number. Please gueass again!")
        print("")
    elif int(user_input_1) == a:
        print("You won! Congratulations! You found the number: " + str(a))
        break
