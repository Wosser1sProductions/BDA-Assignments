def is_unique(l):
    for i in range(len(l)-1):
        for j in range(i):
            if l[i] == l[j]:
                return False     
    return True