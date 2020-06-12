H, W = map(int, input().split())

A = [None] * H
for i in range(H):
    A[i] = list(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
