def is_unique(l):
    checking = []
    for i in range(0, len(l)):
        if i is not checking:
            checking.append(i)
        else:
            return False
    return True