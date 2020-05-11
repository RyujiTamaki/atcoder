"""
N, K = map(int, input().split())
A = list(map(int, input().split()))

A = [a - 1 for a in A]

now = 0
for i in range(K):
    now = A[now]

print(now + 1)
"""



N, K = map(int, input().split())
A = list(map(int, input().split()))

A = [a - 1 for a in A]

now = 0
now_i
passed = []
for i in range(K):
    now = A[now]
    now_i = i
    if now in passed:
        break
    passed.append(now)

print(now + 1)
