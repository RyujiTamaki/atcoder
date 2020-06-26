N, K = map(int, input().split())
h = list(map(int, input().split()))


# 貰うDP
# DP配列全体を初期化
dp = [float("inf")] * (N + K)
# 初期条件を入力
dp[0] = 0

# ループを回す
for i in range(1, N):
    for j in range(1, K + 1):
        try:
            dp[i + j] = min(dp[i + j], dp[i] + abs(h[i] - h[i + j]))
        except IndexError:
            pass

# DPテーブルから解を出力
print(dp[N - 1])
