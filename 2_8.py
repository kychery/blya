def get_partition(s):
    i = 0
    j = 0
    divided_s = []
    while i < len(s):
        i = s.rfind(s[j]) + 1
        if len(set(s[:i]) & set(s[i:])) == 0:
            divided_s.append(s[:i])
            s = s[i:]
            i, j = 0, 0
        else:
            j = j + 1
    return divided_s


S = input('S = ')
print(get_partition(S))
    
