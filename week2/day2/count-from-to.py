x = int(input("Please enter two numbers. First number: "))
y = int(input("Second number: "))

if x >= y:
    print ("The second number should be bigger")
if y > x:
    while x < y:
        print(x)
        x += 1
