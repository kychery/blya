def is_power_of_two(n, a=0, i=0):
    if (n>=0) and (n<1):
        a = 1
        while a >= n:
            a = 2**i
            if n == a:
                return True
            else:
                i -= 1
        return False
    elif n >= 1:
        while a <= n:
            a = 2**i
            if n == a:
                return True
            else:
                i += 1
        return False
    else:
        return False

n = float(input())
is_power_of_two(n)
