def is_prime(x):
    if x < 2:
        return False

    elif x == 2:
        return True

    else:
        for z in range(x-1):
            if x % (z+2) == 0 and x != z+2:
                return False
                break
            elif x % (z+2) == 0 and x == z+2:
                return True


def all_primes_upto(n):
    for z in range(n):
        if is_prime(z+1):
            print(z+1)


def factorize(x):
    pass