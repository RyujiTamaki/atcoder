from itertools import product

N, M, X = map(int, input().split())

C = [None] * N
A = [None] * N
for i in range(N):
    inp = list(map(int, input().split()))
    C[i] = inp[0]
    A[i] = inp[1:]


min_val = sum(C)
ans = False
