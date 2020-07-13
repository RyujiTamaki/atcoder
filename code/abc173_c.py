import numpy as np
from itertools import product
H, W, K = map(int, input().split())

C = [None] * H
for i in range(H):
    C[i] = input()

np_c = np.zeros((H, W), dtype=int)
for i in range(H):
    for j in range(W):
        if C[i][j] == "#":
            np_c[i][j] = 1


ans = 0
for h_bin in product([True, False], repeat = H):
    for w_bin in product([True, False], repeat = W):
        copy_array = np_c.copy()
        for i, h in enumerate(h_bin):
            for j, w in enumerate(w_bin):
                if h:
                    copy_array[i, :] = 0
                if w:
                    copy_array[:, j] = 0
        if copy_array.sum() == K:
            ans += 1

print(ans)
