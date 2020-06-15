X, N = map(int, input().split())

P = list(map(int, input().split()))
candidates = [i for i in range(102)]

ans = 1000
min_diff = 1000
for c in candidates:
    if c in P:
        continue
    diff = abs(X - c)
    if diff < min_diff:
        ans = c
        min_diff = diff

print(ans)
