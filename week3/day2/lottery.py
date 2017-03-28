# Create a method that returns the five most frequent lottery number in a pretty table format
#def five_most_frequent():
#    pass

my_file = 0
a = 0
def five_most_frequent():
    my_file = open("otos.csv", "r")
    test = my_file.readlines()
    n = 0
    g = 0
    p = ""
    for i in test:
        a = test[n]
        n += 1
        g = (a.split(";"))
        print(g[-5 :])
        print(g[-1])


    my_file.close()
five_most_frequent()
