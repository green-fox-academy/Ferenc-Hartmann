# Create a method that returns the five most frequent lottery number in a pretty table format
#def five_most_frequent():
#    pass

my_file = 0
a = 0
k = 0
l = 0
def five_most_frequent():
    my_file = open("lottery.txt", "r")
    test = my_file.readlines()
    n = 0
    g = 0
    numberl = 0
    numberu = 0
    for i in test:
        a = test[n]
        n += 1
        r = 0
        f = ""
        for j in range(15):
            f += a[-(r+1)]
            r += 1
        m = ""
        u = []
        for k in range(15):
            m += f[(-k - 1)]
        g = (m.split(";"))

        m.append((g))
        m += g[-2]
        m += g[-3]
        m += g[-4]
        m += g[-5]
        print(m)



    my_file.close()
five_most_frequent()
