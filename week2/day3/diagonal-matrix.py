
# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

a = []
for x in range(4):
    row = []
    for y in range(4):
        row.append(0)
    a.append(row)


a[0][0] = 1
a[1][1] = 1
a[2][2] = 1
a[3][3] = 1

print (a[0][0], a[0][1], a[0][2], a[0][3])
print (a[1][0], a[1][1], a[1][2], a[1][3])
print (a[2][0], a[2][1], a[2][2], a[2][3])
print (a[3][0], a[3][1], a[3][2], a[3][3])
