import sys
sys.setrecursionlimit(4100000)

N = int(input())
A = list(map(int, input().split()))

dp = [-1] * 81
dp[0] = 1000

for i in range(1, N):
    dp[i] = dp[i - 1]
    for j in range(i):
        kabu = dp[j] // A[j]
        dp[i] = max(dp[i], dp[j] + (A[i] - A[j]) * kabu)

print(dp[N - 1])
