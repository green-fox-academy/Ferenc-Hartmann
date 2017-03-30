# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

base =3
n =  3
def power(n):
    if n == 1: #base case
        return base
    else:
        return (base * power(n-1))

power(n)
print(power(n))
