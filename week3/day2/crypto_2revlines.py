# Create a method that decrypts texts/reversed_zen_lines.txt
#def decrypt(file_name):
#    pass

my_file = 0
def decrypt(file_name):
    my_file = open("reversed-lines.txt", "r")
    test = my_file.readlines()
    n = 0
    for i in test:
        a = test[n]
        n += 1
        p = (len(a))
        r = 0
        f = ""
        for j in range(p):
            f += a[-(r+1)]
            r += 1
        print(f)
decrypt(my_file)
