N, M = map(int, input().split())
H = list(map(int, input().split()))

a = [None] * M
b = [None] * M

ans = {i: True for i in range(N)}

for i in range(M):
    s, t = map(int, input().split())
    a, b = s - 1, t - 1
    if H[a] > H[b]:
        ans[b] = False
    elif H[a] < H[b]:
        ans[a] = False
    elif H[a] == H[b]:
        ans[a] = False
        ans[b] = False

nums = 0
for i in ans.values():
    if i:
        nums += 1

print(nums)
