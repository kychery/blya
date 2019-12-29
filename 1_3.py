def is_power_of_two(n):
    from math import log
    if n > 0:
        a = log(n, 2)
        return a.is_integer()
    else:
        return False

    
a = int(input())
is_power_of_two(a)
