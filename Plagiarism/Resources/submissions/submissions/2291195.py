def is_ordered(l):
    test = True
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            test = True
        else:
            return False
    return test