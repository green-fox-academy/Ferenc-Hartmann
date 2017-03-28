
# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

def divider():
    try:
        n = int(input("Type a number: "))
        a = (10 // n)
        return a
    except ZeroDivisionError:
        return "fail"
print(divider())
