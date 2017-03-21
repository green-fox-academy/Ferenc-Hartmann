x = int(input("Please enter two numbers about the party. Please enter the number of girls coming to the party: "))
y = int(input("Please enter the number of boys coming to the party: "))

if x == y and (x + y) > 20:
    print("The party is exellent!")
if x != y and (x + y) > 20 and x != 0:
    print("Quite cool party!")
if (x + y) < 20 and x != 0:
    print("Average party...")
if x == 0:
    print("Sausage party")
