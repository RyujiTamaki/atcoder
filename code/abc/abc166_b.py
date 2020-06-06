N, K = map(int, input().split())
A = [None] * K
for i in range(K):
    d = int(input())
    A[i] = list(map(int, input().split()))

flat_list = [s for a in A for s in a]
set_a = set(flat_list)
ans = 0

for i in range(1, N + 1):
    if not i in set_a:
        ans += 1

print(ans)
