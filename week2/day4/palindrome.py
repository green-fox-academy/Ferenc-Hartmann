#output = create_palindrome(word)
#print(output) # it prints: pearraep

word = input("Please enter a word to make a palindrome: ")


def create_palindrome(word):
    word = word [::-1]
    return word

print(word + create_palindrome(word))
