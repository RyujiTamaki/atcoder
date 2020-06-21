import itertools

N, K = map(int, input().split())
p = list(map(int, input().split()))

ans = 0
for _ in range(K):
    min_index = p.index(min(p))
    minv = p.pop(min_index)
    ans += minv

print(ans)
