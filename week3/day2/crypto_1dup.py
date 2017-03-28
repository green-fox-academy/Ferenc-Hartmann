# Create a method that decrypts the texts/duplicated_chars.txt

#def decrypt(file_name):
#    pass

my_file = 0
def decrypt(file_name):
    my_file = open("duplicated-chars.txt", "r")
    test = my_file.readlines()
    n = 0
    for i in test:
        a = test[n]
        n += 1
        p = len(a) // 2
        r = 0
        f = ""
        for j in range(p):
            f += a[r]
            r += 2
        print(f)
    my_file.close()
decrypt(my_file)
