x = int(input("Please enter an odd number for the pyramid: "))
a = 0

if x % 2 != 0:
    while a < x:
        a += 1
        print((x-a) * " " + (2 * a - 1) * "*" + (x-a) * " ")
else:
  print("Please restart the program and enter an ODD number.")
