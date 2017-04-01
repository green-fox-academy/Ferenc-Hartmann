students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints:
#  - how many candies they have on average
print(students[0][0])

def masscandy():
    rich = 0
    for i in range(4):
        if students[i]["candies"] > 4:
            rich = students[i]["name"]
            print("They have more than 4 candies: " + str(rich))
masscandy()

def avgcandy():
    rich = 0
    for i in range(4):
        rich += students[i]["candies"]
        if (i +1) == 4:
            rich = (rich / (i +1))
            print("Average candies: " + str(rich))
avgcandy()
