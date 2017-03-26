x = 9

b = 0
a = 0

if x % 2 != 0:
    while a < x:
        a += 2
        print(int((x + 1 - a)/2) * " " + (2 * int(a / 2) - 1) * "*" + int((x + 1 - a)/2) * " ")

if x % 2 != 0:
    while (b + 2) < x:
        b += 2
        print(int(b / 2) * " " + (x - b) * "*" + int(b / 2) * " ")
