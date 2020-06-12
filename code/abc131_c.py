A, B, C, D = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

lcm = C * D // gcd(C, D)

def get_num(X):
    num_c = X // C
    num_d = X // D
    common = X // lcm
    return X - (num_c + num_d) + common


print(get_num(B) - get_num(A - 1))
