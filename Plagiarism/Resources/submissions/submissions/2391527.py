w1 = input("Give a string: ")
w2 = input("Give a string: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"


for char in alphabet:

    count1 = 0
    for i in range(len(w1)):
        if w1[i] == char:
            count1 += 1


    count2 = 0
    for i in range(len(w2)):
        if w2[i] == char:
            count2 += 1

if count1 == count2:
    print(w1, "and", w2, "are anagrams")
    
else:
    print(w1, "and", w2, "are not anagrams")
