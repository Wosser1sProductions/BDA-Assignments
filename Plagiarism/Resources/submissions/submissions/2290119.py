
def is_ordered(l):
    for x in l-1:
        if l[x] > l[x-1]:
            return False
    return True
print(is_ordered(1))