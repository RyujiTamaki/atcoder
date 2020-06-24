from collections import Counter

N = int(input())
A = list(map(int, input().split()))

counter = Counter(A)

all_num = 0
for value in counter.values():
    all_num += value * (value - 1) // 2


for a in A:
    value = counter[a]
    before = value * (value - 1) // 2
    after = (value - 1) * (value -2) // 2
    print(all_num + after - before)
