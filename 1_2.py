def is_beauty(n):
    a = str(abs(n))
    A = 0
    for i in range(len(a)):
        A = A + int(a[i])
    return n % A == 0


is_beauty(145)
