def number_of_matches(J, S):
    n = 0
    for i in range(len(J)):
        for j in range(len(S)):
            if J[i] == S[j]:
                n += 1
    return n

J = str(input('J:'))
s = str(input('S:'))
number_of_matches(J, S)
