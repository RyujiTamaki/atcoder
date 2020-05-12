N, K = map(int, input().split())
A = list(map(int, input().split()))

pos = 0
visit = [0] * N
move = []
roop = []

while visit[pos] != 2:
    if visit[pos] == 0:
        move.append(pos)
    else:
        roop.append(pos)

    visit[pos] += 1
    pos = A[pos] - 1

if len(move) > K:
    print(move[K] + 1)
else:
    print(roop[(K- (len(move) - len(roop))) % len(roop)] + 1)
