def is_unique(l):
    for i in range(len(l)-1):
        for j in i:
            if l[j] == l[i]:
                return False 
    return True