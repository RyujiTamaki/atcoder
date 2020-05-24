N = int(input())
S = input()

ans = 0
for i in range(N):
    a = S[:i]
    b = S[i:]
    c = set(list(a)) & set(list(b))
    ans = max(ans, len(c))

print(ans)
