# Write a recursive function that takes one parameter: n and counts down from n.

number = input("Please enter a positiv number to start the count down from :" )


def counter(n):
    if n == 0: #base case
        #print(n)
        return 0
    else:
        #print(n)
        return (counter(int(n)-1))

counter(number)
