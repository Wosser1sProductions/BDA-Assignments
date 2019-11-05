def merge_lists(first,second):
    if len(first) > len(second):
        newlist = merger(second,first)
    else:
        newlist = merger(first,second)
    return newlist


def merge_sort(l):
    if len(l)<=1:
        return l
    else:
        x = len(l)//2
        léén=merge_sort(l[:x])
        ltwee = merge_sort(l[x:])
        ldrie = merge_lists(léén,ltwee)
        return ldrie

def merger(smal,big):
    i = 0
    j = 0
    newlist = []
    while i < len(smal)-1:
        if smal[i] <= big[j]:
            newlist.append(smal[i])
            i += 1
        else:
            newlist.append(big[j])
            j +=1
    newlist.append(big[j:])
    return newlist
