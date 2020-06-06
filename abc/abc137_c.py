from collections import defaultdict

N = int(input())
ans = 0
d = {}
for _ in range(N):
    s = sorted(input())
    s = "".join(s)
    if s in d:
        ans += d[s]
        d[s] += 1
    else:
        d[s] = 1

print(ans)
