from collections import Counter

N = int(input())
S = []
for _ in range(N):
    S.append(input())

counter = Counter(S)

max_val = max(counter.values())
ans = []
for key, value in counter.items():
    if value == max_val:
        ans.append(key)

ans = sorted(ans)

for s in ans:
    print(s)
