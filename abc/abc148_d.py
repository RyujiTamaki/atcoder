N = int(input())
A = list(map(int, input().split()))

next_break = 1
ans = 0
for a in A:
    if next_break == a:
        next_break += 1
    else:
        ans += 1

if next_break == 1:
    print(-1)
else:
    print(ans)
