#задача4
def is_prime(n):
    if n>0:
        d = 2
        while n % d != 0:
            d += 1
        return d == n
    else:
        return False
is_prime(24)
