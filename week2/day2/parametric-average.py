# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

s = 0
a = 0
number = 0

n = input("Please enter how many numbers do you want to summarize and calculate the average: ")

print("")

while a < int(n):
    number = input("Enter your Number to the Calculation: ")
    a += 1
    s += int(number)

print("")
print("Sum: " + str(s))
print("Average: " + str((int(s) / int(n))))
