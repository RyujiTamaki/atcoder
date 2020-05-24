def preprocess(s):
    if s[0] == "B":
        return -1 * int(s[1]) + 1
    return int(s[0])


S, T = input().split()

S = preprocess(S)
T = preprocess(T)

print(abs(T - S))
