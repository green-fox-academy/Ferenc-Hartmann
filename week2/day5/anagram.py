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

def anagram():
    user_input_0 = input("Please enter the first word to analyse: ")
    print("")
    user_input_1 = input("Please enter the second word to analyse:")
    user_input_1 = user_input_1 [::-1]
    if str(user_input_0) == str(user_input_1):
        return True
    else:
        return False
print(anagram())
