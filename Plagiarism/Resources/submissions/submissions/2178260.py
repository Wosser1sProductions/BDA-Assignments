def is_prime(x):
    if x < 0:
        return False
    elif if x == 1 or x == 2:
        return True
    elif (x % 1 == 0) and (x % x == 0):
        if (x % 2 != 0) and (x % 3 != 0) and (x % 5 != 0) and (x % 7 != 0):
            return True
        else:
            return False