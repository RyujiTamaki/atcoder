import sys
input = sys.stdin.readline

N = int(input())
B = list(map(int, input().split()))

C = [None] * N
C[0] = B[0]
C[-1] = B[-1]

for i in range(1, N - 1):
    C[i] = min(B[i - 1], B[i])

print(sum(C))
