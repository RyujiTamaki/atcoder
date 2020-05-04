import collections

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(M)]

a = [v[0] for v in ab]
b = [v[1] for v in ab]
a.extend(b)
c = collections.Counter(a)

for i in range(1, N + 1):
    print(c[i])
