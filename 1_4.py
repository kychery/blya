def is_prime(n, d=2):
    if n > 1:
        while n % d != 0:
            d += 1
        return True
    else:
        return False
    

num = int(input())
is_prime(num)
