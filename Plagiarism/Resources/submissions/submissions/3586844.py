def is_prime(x):
    if x <= 1:
        return False
        
    for i in range(2, x):
        if (x % i == 0 and x != i) or x < 0:
            return False
    return True


def all_primes_upto(x):
    for i in range(x):
        if (is_prime(i)):
            print(i)


def factorize(x):
    number = x
    for i in range(x):
        if is_prime(i) and number % i == 0:
            number -= i
            print(i)
            
            
            