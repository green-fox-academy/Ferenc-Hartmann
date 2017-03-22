
# - Create a function called `factorio`
#   that returns it's input's factorial


p = int(input("Tell me the number until you want to factorial the numbers please: "))

def factorio(p):
    x = 1
    y = 1
    while x < p:
        x += 1
        y *=x
    print(y)

factorio(p)
