# Create a method that decrypts the texts/duplicated_chars.txt

#def decrypt(file_name):
#    pass

my_file = 0
def decrypt(file_name):
    my_file = open("duplicated-chars.txt", "r")
    lines = my_file.readlines()
    linecount = 0
    for line in lines:
        oneline = lines[linecount]
        linecount += 1
        halflinelength = len(oneline) // 2
        charcount = 0
        fulltext = ""
        for char in range(halflinelenth):
            fulltext += oneline[charcount]
            charcount += 2
        print(fulltext)
    my_file.close()
decrypt(my_file)
