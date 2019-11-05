import math
import string
alfabet="abcdefghijklmnopqrstuvwxyz"

def find(s, ch):
    x = 0
    while x < len(s):
        if s[x] == ch:
            return x
        x += 1
    return -1
def encode(s,n):
    antwoord = ""
    nieuw = ""
    if n < 0:
        n=n + 26*abs(math.floor(n/26))
    elif n > 25:
        n = n - 26*math.floor(n/26)
    for p in s:
        if p == " ":
            antwoord = antwoord + " "
        elif p in string.punctuation:
            nieuw = antwoord[:] + p
            antwoord = nieuw
        else:
            g = find(alfabet, p) + n
            if g > 25:
                g = g - 26
            nieuw = antwoord[:] + alfabet[g]
            antwoord = nieuw
    return nieuw
def decode(s,n):
    antwoord = ""
    nieuw = ""
    if n < 0:
        n=n + 26*abs(math.floor(n/26))
    elif n > 25:
        n = n - 26*math.floor(n/26)
    for p in s:
        if p == " ":
            antwoord = antwoord + " "
        elif p in string.punctuation:
            nieuw = antwoord[:] + p
            antwoord = nieuw
        else:
            g = find(alfabet, p) - n
            if g < 0:
                g = g + 26
            nieuw = antwoord[:] + alfabet[g]
            antwoord = nieuw
    return nieuw