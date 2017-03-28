# write a function that takes a filename and returns the number of lines the
# file contains. It should return zero if the file does not exist.

def liner():
        try:
            my_file = 0
            filename = str(input("Please give me the filename: "))
            my_file = open(filename, "r")
            lines = my_file.readlines()
            counter = 0
            for i in lines:
                counter += 1
            return ("Lines in file: " + str(counter))
        except FileNotFoundError:
            return "0"
print(liner())
