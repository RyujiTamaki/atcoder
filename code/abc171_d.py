from collections import Counter

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = []
C = []
for _ in range(Q):
    b, c = map(int, input().split())
    B.append(b)
    C.append(c)

counter = Counter(A)
ans = 0
for num, count in counter.items():
    ans += num * count

for i in range(Q):
    if B[i] in counter:
        ans += counter[B[i]] * C[i] - counter[B[i]] * B[i]
        counter[C[i]] = counter[C[i]] + counter.pop(B[i])
    print(ans)
