def shift(l, n):
    n %= len(l)
    newlist = [0 for x in range(len(l))]
    for i in range(len(l)):
        if i+n >= 0:
            if i < len(l):
                newlist[i+n] = l[i]
            elif i >= len(l):
                newlist[i+n] = l[i-len(l)]
        if i+n < 0:
            if i >= 0:
                newlist[i+n] = l[i]
            elif i < 0:
                newlist[i+n] = l[i+len(l)]
        
    return newlist