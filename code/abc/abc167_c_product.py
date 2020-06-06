from itertools import product
import numpy as np

N, M, X = map(int, input().split())

C = [None] * N
A = [None] * N
for i in range(N):
    inp = list(map(int, input().split()))
    C[i] = inp[0]
    A[i] = inp[1:]

C = np.array(C)
A = np.array(A)
ans = C.sum() + 1

for choices in product((True, False), repeat=N):
    choices = np.array(list(choices), dtype=bool)
    if np.all(A[choices, :].sum(axis=0) >= X):
        ans = min(ans, C[choices].sum())

if ans == C.sum() + 1:
    print(-1)
else:
    print(ans)
