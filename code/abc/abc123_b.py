import itertools

A = [None] * 5
for i in range(5):
    A[i] = int(input())

ans = 10000

for a in itertools.permutations(A):
    total = 0
    for t in a:
        while total % 10 != 0:
            total += 1
        total += t
    ans = min(ans, total)

print(ans)
