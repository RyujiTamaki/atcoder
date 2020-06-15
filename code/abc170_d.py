from collections import Counter

N = int(input())
A = list(map(int, input().split()))

# 同じ値が複数存在するかチェックする用のカウンタ
counter = Counter(A)

# dp[a] = True: Aにaより小さいaの約数が存在する
A_max = max(A)
dp = {a: False for a in A}

for a in A:
    # xが数列Aに含まれているとき、aより大きいaの倍数tについて、dp[a * t]をTrueに変更する
    if counter[a] > 0:
        t = 2
        while a * t <= A_max:
            dp[a * t] = True
            t += 1

ans = 0
for a in A:
    if counter[a] == 1 and dp[a] is False:
        ans += 1

print(ans)
