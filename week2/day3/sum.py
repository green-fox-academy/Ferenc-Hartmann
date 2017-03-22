
# - Write a function called `sum` that sum all the numbers
#   until the given parameter


p = int(input("Tell me the number until you want to summarize the numbers please: "))

def sum(p):
    x = 0
    y = 0
    while x < p:
        x += 1
        y +=x
    print(y)
sum(p)
