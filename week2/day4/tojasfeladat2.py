#függvény: szummázás

number = 5

def sum(n):
    out = 0
    for i in range(1, n + 1):
        out += i
    return out



print(sum(number))
