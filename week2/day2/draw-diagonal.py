# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was

x = int(input("Please enter a number for the square: "))
a = 0

print((x-1) * "%")

while a < (x - 2):
    a += 1
    print("%" + (a-1) * " " + ((((2 * x) - 3) // (a + x)) * "%") + ((x - 3) - a) * " " + "%")

print((x-1) * "%")
