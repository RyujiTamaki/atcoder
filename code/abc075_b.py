H, W = map(int, input().split())

S = [list(input()) for i in range(H)]
ans = [["#"] * W for i in range(H)]

dx = [1, 0, -1, 0, 1, -1, -1, 1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue

        num = 0
        for d in range(8):
            ni = i + dy[d]
            nj = j + dx[d]

            if ni < 0 or H <= ni:
                continue

            if nj < 0 or W <= nj:
                continue

            if S[ni][nj] == "#":
                num += 1

        ans[i][j] = str(num)

for i in range(H):
    print("".join(ans[i]))
