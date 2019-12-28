def number_of_matches(J, S):
    count = 0
    for i in range(len(J)):
        for j in range(len(S)):
            if J[i] == S[j]:
                count += 1
    return count

J = input("J =")
S = input("S =")
print(number_of_matches(J, S))
