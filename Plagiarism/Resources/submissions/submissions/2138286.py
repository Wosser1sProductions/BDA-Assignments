amount = 0
word = input()
i = 0
for letter in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
    while i < len(word):
        if word[i] == letter:
            amount += 1
        i += 1
    print(letter + ": " + str(amount))
    amount = 0
    i = 0