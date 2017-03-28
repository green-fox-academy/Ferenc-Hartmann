# Create a method that decrypts texts/encoded_zen_lines.txt
#def decrypt(file_name):
#    pass


my_file = 0
def decrypt(file_name):
    my_file = open("encoded-lines.txt", "r")
    lines = my_file.readlines()
    linecount = 0
    for line in lines:
        oneline = lines[linecount]
        linecount += 1
        linelength = len(oneline)
        charcount = 0
        fulltext = ""
        onechar = 0
        char2 = 0
        char1 = 0
        for j in range(linelength):
            onechar = oneline[charcount]
            char1 = ord(onechar)
            if onechar == " ":
                char2 = chr(char1)
            else:
                char2 = chr(char1 - 1)
            fulltext += char2
            charcount += 1
        print(fulltext)
    my_file.close()
decrypt(my_file)
