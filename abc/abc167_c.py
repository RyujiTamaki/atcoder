N, M, X = map(int, input().split())

C = [None] * N
A = [None] * N
for i in range(N):
    inp = list(map(int, input().split()))
    C[i] = inp[0]
    A[i] = inp[1:]


min_val = sum(C)
ans = False

for bit in range(1 << N):
    R = [0] * M
    c = 0

    for i in range(N):
        if bit & (1 << i):
            c += C[i]
            for m in range(M):
                R[m] += A[i][m]

    if all([r >= X for r in R]):
        ans = True
        min_val = min(min_val, c)


if ans:
    print(min_val)
else:
    print('-1')
