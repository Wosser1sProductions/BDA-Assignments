def is_prime(x):
    if x == 1:
        return True
    if x < 1:
        return False
        
    
    for i in range(2, x):
        if x % i == 0 and x != i:
            return False
    return True

def all_primes_upto(x):
    pass


def factorize(x):
    pass