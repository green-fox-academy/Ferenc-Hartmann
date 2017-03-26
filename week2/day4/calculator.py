
# Create a simple calculator application which does read the parameters from the prompt
# and prints the result to the prompt.

# It should support the following operations:
# +, -, *, /, % and it should support two operands.

# The format of the expressions must be: {operation} {operand} {operand}.
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit

user_input = input("Please type in the expression in the format like '+ 3 3':")

a = user_input[0]
b = user_input[2]
c = user_input[4]
d = 0

if a == "+":
    d = int(b) + int(c)
    print(d)
elif a == "-":
    d = int(b) - int(c)
    print(d)
elif a == "*":
    d = int(b) * int(c)
    print(d)
elif a == "/":
    d = int(b) / int(c)
    print(d)
elif a == "%":
    d = int(b) % int(c)
    print(d)
else:
    print("Please type in format {operation} {operand} {operand}")
