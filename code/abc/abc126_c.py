N, K = map(int, input().split())

probs = 0
for i in range(1, N + 1):
    point = i
    cnt = 0
    while point < K:
        point *= 2
        cnt += 1
    probs += (1 / N) * (0.5 ** cnt)

print(probs)
