def is_prime(x):
    if x > 1:
        for i in range (2,(x-1)):
            if x%i == 0:
                return False
        return True
    return False
    
def all_primes_upto(x):
    for i in range (0,x):
        priem == is_prime(i)
        if priem:
            print(i)


def factorize(x):
    pass