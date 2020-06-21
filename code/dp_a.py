N = int(input())
h = list(map(int, input().split()))

"""
# 貰うDP
# DP配列全体を初期化
dp = [float("inf")] * N
# 初期条件を入力
dp[0] = 0
dp[1] = abs(h[1] - h[0])

# ループを回す
for i in range(2, N):
    dp[i] = min(dp[i - 2] + abs(h[i] - h[i - 2]), dp[i - 1] + abs(h[i] - h[i - 1]))
"""

# 貰うDP
# DP配列全体を初期化
dp = [float("inf")] * N
# 初期条件を入力
dp[0] = 0

# ループを回す
for i in range(N - 1):
    if i == N - 2:
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]))
    else:
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]))
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]))


# DPテーブルから解を出力
print(dp[N - 1])
