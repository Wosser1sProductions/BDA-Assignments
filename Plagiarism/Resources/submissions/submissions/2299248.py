def is_unique(l):
    for i in range(0, len(l)):
        if l[len(l)-1] == l[(len(l)-1)-i]:
            return False
    return True