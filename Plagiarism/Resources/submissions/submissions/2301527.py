def lucky_numbers(n):
    l = []
    for i in range(1,n+1):
        l += [i]
    teller = n
    for j in range(1, n+1):
        if teller == teller-teller//j:
            return l
        else:
            for k in range(1, teller//j):
                del l[k]
        teller = teller-teller//j