def is_unique(l):
    for i in l:
        for j in l:
            if i != j:
                if j <= len(l) and i < len(l):
                    print(i)
                    print(j)
                    if l[i-1] == l[j-1]:
                        return False
    return True