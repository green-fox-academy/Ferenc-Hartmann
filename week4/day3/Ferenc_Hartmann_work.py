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

class Letter_Counter():
    def lc(self, a=""):
        letter_numbers = {}
        x = len(a)
        y = 0
        for i in a:
            maxcharcounter = 1
            charcounter = 1
            for j in range((y+1),x):
                if (y+1) == x:
                    maxcharcounter = charcounter
                elif i == a[int(j)]:
                    charcounter += 1
                maxcharcounter = charcounter
            y +=1
            letter_numbers[i] = maxcharcounter
        y = 0
        for i in a:
            maxcharcounter = 1
            charcounter = 1
            for j in range((y+1),x):
                if (y+1) == x:
                    maxcharcounter = charcounter
                elif i == a[int(j)]:
                    charcounter += 1
                maxcharcounter = charcounter
            y +=1
            if letter_numbers[str(i)] < maxcharcounter:
                letter_numbers[i] = maxcharcounter
        return (letter_numbers)

class Fibonacci():
    def fibonacci_m(self, n):
        if n == 0 or n == 1: #base case
            return n
        if n < 0 or n/1 != n//1:
            return ("Try with a natural number")
        else:
            return ((self.fibonacci_m(n-1) + self.fibonacci_m(n-2)))
