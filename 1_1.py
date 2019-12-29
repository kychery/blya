#задача1
def get_digit_sum(n):
    a=str(abs(n))
    A=0
    for i in range(len(a)):
        A=A+int(a[i])
    return A


get_digit_sum(-1289)
