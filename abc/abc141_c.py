from collections import Counter
import sys
input = sys.stdin.readline

N, K, Q = map(int, input().split())

points = [None] * N
A = [None] * Q

for i in range(Q):
    A[i] = int(input())

counter = Counter(A)

for i in range(N):
    points[i] = K - Q + counter[i + 1]

for p in points:
    if p > 0:
        print("Yes")
    else:
        print("No")
