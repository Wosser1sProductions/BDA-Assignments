def is_unique(l):
    element_count = 0
    for element1 in l:
        for element2 in l:
            if element1 == element2:
                element_count += 1
        element_count = 0
        if element_count != 1:
            return False
    return True