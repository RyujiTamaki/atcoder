A, B, K = map(int, input().split())

ans = []
end = A + K if A + K < B else B
for a in range(A, end):
    ans.append(a)

start = B - K + 1 if B - K + 1 > A else A
for b in range(start, B + 1):
    ans.append(b)

for a in sorted(set(ans)):
    print(a)
