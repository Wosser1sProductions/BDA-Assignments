string1 = input("Geef een string: ")
string2 = input("Geef een andere string: ")
alfabet = "abcdefghijklmnopqrstuvwxyz"
anagram = True
for char in string1:
    count2 = 0
    for i in range(len(string2)):
        if char in string2[i]: 
            count2 += 1
    count1 = 0
    for i in range(len(string1)):
        if char in string1[i]:
            count1 += 1
    if count1 != count2:
        anagram = False
anagram is True:
    print(string1, "and", string2, "are anagrams")
else:
    print(string1, "and", string2, "are not anagrams")
