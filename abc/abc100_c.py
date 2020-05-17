def calc(x):
    cnt = 0
    while x % 2 == 0:
        x = x // 2
        cnt += 1
    return cnt


N = int(input())
a = list(map(int, input().split()))
ans = 0

for i in range(N):
    ans += calc(a[i])

print(ans)
