def verplaatsinglinks(l):
    k = l + []
    for i in range(len(l)):
        if i-1 < 0:
            k[i] = l[len(l-1)]
        else:
            k[i] = l[i-1]
    return k

def verplaatsingrechts(l):
    k = l + []
    for i in range(len(l)):
        if i+1 >= len(l):
            k[i] = l[0]
        else:
            k[i] = l[i+1]
    return k

def shift(l, n):
    if n >= 0:
        for j in range(n+1):
            l = verplaatsingrechts(l)
    else:
        for j in range(n):
            l = verplaatsinglinks(l)
    return l
    