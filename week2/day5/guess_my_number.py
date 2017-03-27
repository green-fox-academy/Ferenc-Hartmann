#2XP
#Exercise
#Write a program where the program chooses a number between 1 and 100. The player is then asked to enter a guess. If the #player guesses wrong, then the program gives feedback and ask to enter an other guess until the guess is correct.
#Make the range customizable (ask for it before starting the guessing).
#You can add lives. (optional)
#Example
#I've the number between 1-100. You have 5 lives.
#20
#Too high. You have 4 lives left.
#10
#Too low. You have 3 lives left.
#15
#Congratulations. You won!

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
