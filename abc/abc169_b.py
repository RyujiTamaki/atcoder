N = int(input())
A = list(map(int, input().split()))

ans = 1

min_A = min(A)
A = sorted(A, reverse=True)

if min_A == 0:
    print(0)
    exit()

for a in A:
    ans *= a
    if ans > 10 ** 18:
        break

if ans > 10 ** 18:
    print(-1)
else:
    print(ans)
