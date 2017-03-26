# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

a = 0

while a < 100:
    a += 1
    if (a / 3) == (a // 3) and (a / 5) == (a // 5):
        print("FizzBuzz")
    elif (a / 3) == (a // 3):
        print("Fizz")
    elif (a / 5) == (a // 5):
        print("Buzz")
    else:
        print(a)
