Word1 = input("Give the first word: ")
Word2 = input("Give the second word: ")
Word1Sort = sorted(Word1)
Word2Sort = sorted(Word2)
if Word1Sort == Word2Sort:
    print(Word1, "and", Word2, "are anagrams")
else:
    print(Word1, "and", Word2, "are not anagrams")
