import queue

N, M = map(int, input().split())

graph = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

# 各部屋に設定する番号を記録する
v = [-1 for i in range(N)]  # 全頂点を「未訪問」に初期化
v[0] = 0  # スタート地点を0にする
# queueを作成し部屋1（インデックスは0）を入れる
q = queue.Queue()
q.put(0)

while not q.empty():
    # queueの先頭（今いる部屋の番号）を取り出す
    x = q.get()
    # 今いる部屋と繋がっている部屋を順に探索する
    for y in graph[x]:
        # -1 でない場合は探索済みなのでスキップする
        if v[y] != -1:
            continue
        # あとで探索するためにqueueに入れておく
        q.put(y)
        v[y] = x

print("Yes")
for i in range(1, N):
    print(v[i] + 1)
