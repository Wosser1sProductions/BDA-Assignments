def is_prime(x):
# declerations

#function looks for prime
    if x > 1:
        for i in range(x-1):
            if x % (i+1) == 0 and i+1 != 1 and i+1 != x:
                return False
        return True
    else:
        return False

def all_primes_upto(x):
    for i in range(x):
        if is_prime(i) == True:
            print(i)


def factorize(x):
    pass