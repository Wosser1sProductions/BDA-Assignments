def is_ordered(list):
    for i in range(0,len(list)-1):
        if list[i] <= list[i+1]:
            continue
        else:
            return False
    return True
