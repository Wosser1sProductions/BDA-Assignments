word = input("give a word: ")
length_word = len(word)
reverse = ""
for i in range(length_word):
    reverse += word[length_word -1 -i]
if (reverse == word):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")