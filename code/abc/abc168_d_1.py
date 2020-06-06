import queue

N, M = map(int, input().split())

graph = [[] for i in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

dist = [-1 for i in range(N)]
que = queue.Queue()

dist[0] = 0
que.put(0)


while not que.empty():
    v = que.get()
    for nv in graph[v]:
        if dist[nv] != -1:
            continue

        dist[nv] = v
        que.put(nv)


print("Yes")
for i in range(1, N):
    print(dist[i] + 1)
