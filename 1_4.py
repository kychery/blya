def is_prime(n):
    if n > 1:
        d = 2
        while n % d != 0:
            d += 1
        return d == n
    else:
        return False
    

num = int(input())
is_prime(num)
