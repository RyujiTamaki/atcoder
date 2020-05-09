def manhattan_distance(s, c):
    return abs(s[0] - c[0]) + abs(s[1] - c[1])


N, M = map(int, input().split())

students = [list(map(int, input().split())) for _ in range(N)]
checkpoints = [list(map(int, input().split())) for _ in range(M)]

for s in students:
    ans = 0
    min_distance = manhattan_distance(s, checkpoints[0])
    for i in range(1, M):
        distance = manhattan_distance(s, checkpoints[i])
        if min_distance > distance:
            min_distance = distance
            ans = i
    print(ans + 1)
