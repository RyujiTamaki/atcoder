N, A, B = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    num = str(i)
    total = 0
    for n in num:
        total += int(n)
    if total >= A and total <= B:
        ans += i

print(ans)
