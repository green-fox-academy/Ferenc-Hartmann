# Create a method that decrypts texts/encoded_zen_lines.txt
#def decrypt(file_name):
#    pass


my_file = 0
def decrypt(file_name):
    my_file = open("encoded-lines.txt", "r")
    test = my_file.readlines()
    n = 0
    for i in test:
        a = test[n]
        n += 1
        p = len(a)
        r = 0
        f = ""
        ch = 0
        ch2 = 0
        ch1 = 0
        for j in range(p):
            ch = a[r]
            ch1 = ord(ch)
            if ch == " ":
                ch2 = chr(ch1)
            else:
                ch2 = chr(ch1 - 1)
            f += ch2
            r += 1
        print(f)
    my_file.close()
decrypt(my_file)
