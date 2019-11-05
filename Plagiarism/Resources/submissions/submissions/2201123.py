import math

letters = "abcdefghijklmnopqrstuvwxyz"
def encode(s, n):
    newword = ""
    subword = ""
    for i in range(len(s)):
        if s[i] not in letters:
            newword += s[i]
        elif ord(s[i]) + n > ord("z"):
            newword += chr(ord(s[i]) - (((ord(s[i]) - 26 + n) // ord("z"))+1)*26 + n)
        elif ord(s[i]) + n < ord("a"):
            newword += chr(ord(s[i]) + 26 + n)
        else:
            newword += chr(ord(s[i]) + n)
    return newword

def decode(s,n):
    newword = ""
    for i in range(len(s)):
        if s[i] not in letters:
            newword += s[i]
        elif ord(s[i]) - n > ord("z"):
            newword += chr(ord(s[i]) - (((ord(s[i]) - 26 + n) // ord("z"))+1)*26 - n)
        elif ord(s[i]) - n < ord("a"):
            newword += chr(ord(s[i]) + 26 + n)
        else:
            newword += chr(ord(s[i]) - n)
    return newword


