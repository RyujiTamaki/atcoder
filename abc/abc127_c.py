N, M = map(int, input().split())

left = 1
right = N

for i in range(M):
    L, R = map(int, input().split())
    left = max(left, L)
    right = min(right, R)

print(max(right - left + 1, 0))
