# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

string = "Please xummi the xummi of bunnies to xummi their xummies :"
def normalstringer(n):
    def stringer(n):
        stringy = ""
        if len(stringy) == len(n): #base case
            return ""
        else:
            stringy += "*" + n[(len(n)-1)]
            return stringy +(stringer(n[0:(len(n)-1)]))
    return stringer(n)[::-1]
print(normalstringer(string))
