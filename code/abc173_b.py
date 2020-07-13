from collections import Counter

N = int(input())
S = [None] * N
for i in range(N):
    s = input()
    S[i] = s

counter = Counter(S)

cases = ["AC", "WA", "TLE", "RE"]
for case in cases:
    if case in counter:
        print(f"{case} x {counter[case]}")
    else:
        print(f"{case} x 0")
