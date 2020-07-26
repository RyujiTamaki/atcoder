N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A = [a - 1 for a in A]

ans = B[A[0]]
for i in range(1, N):
    ans += B[A[i]]
    if A[i] == A[i - 1] + 1:
        ans += C[A[i - 1]]

print(ans)
