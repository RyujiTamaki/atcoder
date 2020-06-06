A, B, C = map(int, input().split())

ans = False
for i in range(A * B + 1):
    if (A * i) % B == C:
        ans = True

if ans:
    print("YES")
else:
    print("NO")
