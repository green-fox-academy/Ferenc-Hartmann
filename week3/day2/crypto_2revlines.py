# Create a method that decrypts texts/reversed_zen_lines.txt
#def decrypt(file_name):
#    pass

my_file = 0
def decrypt(file_name):
    my_file = open("reversed-lines.txt", "r")
    lines = my_file.readlines()
    linecount = 0
    for line in lines:
        oneline = lines[linecount]
        linecount += 1
        linelength= (len(oneline))
        charcount = 0
        fulltext = ""
        for char in range(linelength):
            fulltext += oneline[-(charcount + 1)]
            charcount += 1
        print(fulltext)
    my_file.close()
decrypt(my_file)
