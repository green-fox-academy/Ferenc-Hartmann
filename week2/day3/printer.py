
# - Create a function called `printer`
#   which prints the input parameters
#   (can have multiple number of arguments)

a1 = input("Enter 4 numbers to print. Enter first number please: ")
a2 = input("Enter Second number please: ")
a3 = input("Enter third number please: ")
a4 = input("Enter fourth number please: ")

def printer(a1, a2, a3, a4):
    list=[a1, a2, a3, a4]
    print(list)

printer(a1, a2, a3, a4)
