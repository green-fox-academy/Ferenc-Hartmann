
# Check if the list contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

testlist = [1, 4, 7, "abc"]

n = len(testlist)
s = 0

for i in range(n):
    if testlist[i] == 7:
        s +=1
if s > 0:
    print("Hoorray")
else:
    print("Noooooo")
