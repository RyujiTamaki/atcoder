import math


N, D = map(int, input().split())
X = [None] * N

for i in range(N):
    X[i] = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        total = 0
        for k in range(D):
            total += (X[i][k] - X[j][k]) * (X[i][k] - X[j][k])
        distance = math.sqrt(total)
        if distance.is_integer():
            ans += 1

print(ans)
