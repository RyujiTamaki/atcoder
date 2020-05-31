# pythonだとデフォルトの再帰処理回数の上限に引っかかってしまうので、それを変更
import sys
sys.setrecursionlimit(1000000)


def dfs(x, y):
    reached[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # nx と ny が街の範囲内か、行ったことがないか、塀ではないかを判定
        if 0 <= nx and nx < H and 0 <= ny and ny < W and reached[nx][ny] is False and c[nx][ny] != "#":
            dfs(nx, ny)


H, W = map(int, input().split())
c = [list(input()) for i in range(H)]
reached = [[False] * W for i in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(H):
    for j in range(W):
        if c[i][j] == "s":
            dfs(i, j)

for i in range(H):
    for j in range(W):
        if c[i][j] == "g" and reached[i][j]:
            print("Yes")
            exit()
print("No")
