N = int(input())
A = list(map(int, input().split()))

total_minus_num = 0
B = []
for a in A:
    if a < 0:
        total_minus_num += 1
    B.append(abs(a))

ans = sum(B)
if total_minus_num % 2 == 0:
    print(ans)
else:
    print(ans - 2 * min(B))
