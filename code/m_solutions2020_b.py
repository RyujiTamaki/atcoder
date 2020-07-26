A, B, C = map(int, input().split())
K = int(input())

ans = False
for i in range(K):
    if A < B < C:
        ans = True
        break

    if B <= A:
        B *= 2
    elif C <= B:
        C *= 2

if A < B < C:
    ans = True


if ans:
    print("Yes")
else:
    print("No")
