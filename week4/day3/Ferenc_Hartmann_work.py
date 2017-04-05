class Needtest():
    def get_apple(Self):
        return "apple"

class Summarize():
    def sum(Self, a=[0]):
        summed = 0
        for i in range(len(a)):
            summed += a[i]
        return summed

class Anagram():
    def anag(self, a="", b=""):
        a_letters = []
        b_letters = []
        x = 0
        y = 0
        for i in a:
            if a[int(x)] == " ":
                pass
            else:
                a_letters.append(a[int(x)])
            x +=1
        a_letters = sorted(a_letters)
        for j in b:
            if b[int(y)] == " ":
                pass
            else:
                b_letters.append(b[int(y)])
            y +=1
        b_letters = sorted(b_letters)
        if a_letters == b_letters:
            return True
        else:
            return False

class Letter_counter():
    def lc(self, a=""):
        letter_numbers = {}
        x = 0
        y = 1
        charcounter = 1
        maxcharcounter = 0
        sorted_a = sorted(a)
        print(sorted_a)
        for i in sorted_a:
            print(i)
            if i == " ":
                pass
            else:
                if sorted_a[int(x)] == sorted_a[(int(y))]:
                    charcounter += 1
                    if charcounter > maxcharcounter:
                        maxcharcounter = charcounter
                    print(maxcharcounter)
                    letter_numbers[sorted_a[int(x)]] = int(charcounter)
                else:
                    charcounter = 1
                    letter_numbers[sorted_a[int(x)]] = int(charcounter)
            x += 1
            y += 1
        return letter_numbers


cucu = Letter_counter()
cucu.lc("ciamicac")
