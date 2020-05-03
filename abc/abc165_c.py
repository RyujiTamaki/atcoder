import itertools


N, M, Q = map(int, input().split())

a = [None] * Q
b = [None] * Q
c = [None] * Q
d = [None] * Q

for i in range(Q):
    num = list(map(int, input().split()))
    a[i], b[i], c[i], d[i] = num[0] - 1, num[1] - 1, num[2], num[3]

A = [i for i in range(1, M + 1)]

max_v = 0
for v in itertools.combinations_with_replacement(A, N):
    tmp_sum = 0
    for i in range(Q):
        if v[b[i]] - v[a[i]] == c[i]:
            tmp_sum += d[i]
    max_v = max(max_v, tmp_sum)

print(max_v)
