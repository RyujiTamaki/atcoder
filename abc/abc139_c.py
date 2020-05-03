import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

max_step = 0
step = 0

for i in range(1, N):
    if A[i] > A[i - 1]:
        step = 0
    else:
        step += 1
    max_step = max(max_step, step)

print(max_step)
