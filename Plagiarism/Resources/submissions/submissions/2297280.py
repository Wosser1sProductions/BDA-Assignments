def is_ordered(l):
    for i in range(l, len(l)):
        return l[i] >= l[i-1] or l[i] <= l[i-1] == 0
        