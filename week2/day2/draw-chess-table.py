
# Crate a program that draws a chess table like this
#
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
#

size = 8
a = 0

while a < int(size):
    a += 2
    print((int(size) // 2) * "% ")
    print((int(size) // 2) * " %")
