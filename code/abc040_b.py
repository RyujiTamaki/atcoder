n = int(input())

ans = n ** 2
for h in range(1, n + 1):
    w = n // h
    ans = min(ans, abs(h - w) + (n - h * w))

print(ans)
