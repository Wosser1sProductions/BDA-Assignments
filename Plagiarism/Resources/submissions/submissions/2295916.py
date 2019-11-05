def shift(l, n):
    shifted_list = []
    list_len = len(l)
    
    for index, element in enumerate(l):
        shifted_list.append( l[(index + n - 1) % list_len] )
    
    return shifted_list