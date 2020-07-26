N, K = map(int, input().split())
A = list(map(int, input().split()))

cumsum = [0 for _ in range(N + 1)]
for i in range(N):
    cumsum[i + 1] = cumsum[i] + A[i]

for i in range(N):
    if i <= K - 1:
        continue

    prev = cumsum[i] - cumsum[i - K]
    now = cumsum[i + 1] - cumsum[i - K + 1]
    if now > prev:
        print("Yes")
    else:
        print("No")
