N, M, Q = map(int, input().split())

# ある人がどの問題を解いたのか
solved = [[] for _ in range(N)]
# どの問題が何人に解かれたのか
cnt = [0 for _ in range(M)]


for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        query[1] -= 1
        ans = 0
        for s in solved[query[1]]:
            ans += N - cnt[s]
        print(ans)
    else:
        query[1] -= 1
        query[2] -= 1
        cnt[query[2]] += 1
        solved[query[1]].append(query[2])
