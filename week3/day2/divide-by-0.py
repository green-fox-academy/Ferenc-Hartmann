
# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0
n = 2
a = 0
#def divider():
def divider():
    while True:
        try:
            n = int(input("Type a number: "))
            a = (10 // n)
            print(a)
            break
        except ZeroDivisionError:
            print("fail")
divider()
