# Given a non-negative int n, return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while
# divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

number = int(input("Please enter a positiv number to sum the digits :" ))

def sumdigit(n):
    sum = 0
    if n < 10: #base case
        return n
    else:
        return ((int(n) % 10) + sumdigit(int(n)//10))

sumdigit(number)
print(sumdigit(number))
