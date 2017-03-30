# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

number = input("Please enter a positiv number to start the count down from :" )

def counter(n):
    if n == 1: #base case
        return 1
    else:
        return (int(n) + (counter(int(n)-1)))

counter(number)
print(counter(number))
