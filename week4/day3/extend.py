
# Adds a and b, returns as result
def add(a, b):
    return a+b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > b and c > a:
        return c

# Returns the median value of a list given as param
def median(pool=[]):
    p = 0
    x = 0
    for i in pool:
        p += pool[int(x)]
        x +=1
    f = (p/len(pool))
    return f

# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aeiou'


# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve
