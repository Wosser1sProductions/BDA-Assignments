def is_unique(l):
    for value in range(len(l)):
        if l[value] in l[:value] or value in l[value+1:]:
            return False
    
    return True
            