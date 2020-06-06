from collections import Counter

N = int(input())
A = list(map(int, input().split()))

counter = Counter(A)

for a in A:
    counter[a - 1] += 1
    counter[a + 1] += 1

print(max(counter.values()))
