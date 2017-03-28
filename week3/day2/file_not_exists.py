# write a function that takes a filename and returns the number of lines the
# file contains. It should return zero if the file does not exist.
n = 2

def liner():
    while True:
        try:
            my_file = 0
            filename = str(input("Please give me the filename: "))
            my_file = open(filename, "r")
            test = my_file.readlines()
            n = 0
            for i in test:
                n += 1
            print("Lines in file: " + str(n))
            break
        except FileNotFoundError:
            print("0")
liner()
