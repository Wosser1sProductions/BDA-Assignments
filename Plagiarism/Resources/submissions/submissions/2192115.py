import string

def count_words(string):
    split_string = string.split
    x = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 "
    for i in string:
        if len(string) >= 2:
            if i not in alphabet:
                x += 1
        elif len(string) == 0:
                x = -1
        elif len(string) == 1:
                x = 0
    return x+1
