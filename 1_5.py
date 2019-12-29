def is_self_dividing(n):
    a = str(abs(n))
    x = 0
    for i in range(len(a)):
        if n % int(a[i]) != 0:
            x = x + 1
    return x == 0


is_self_dividing(16)
