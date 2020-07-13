import sys
import numpy as np

input = sys.stdin.readline


def f(A, N, K):
    A = sorted(A, key=abs, reverse=True)
    if N == K:
        return A
    A = np.array(A)
    if np.all(A < 0):
        if K % 2 == 0:
            return A[:K]
        else:
            return A[-K:]

    pos = A[A >= 0]
    neg = A[A < 0]
    nums = [1]

    if K & 1:
        nums = [pos[0]]
        pos = pos[1:]
        K -= 1

    


N, K = map(int, input().split())
A = list(map(int, input().split()))

B = f(A, N, K)
