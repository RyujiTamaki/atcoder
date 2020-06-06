S = input()
N = len(S)

s1 = "01" * (N // 2)
s2 = "10" * (N // 2)

if N % 2 == 1:
    s1 += "0"
    s2 += "1"

diff1 = 0
diff2 = 0

for i in range(N):
    if S[i] != s1[i]:
        diff1 += 1
    if S[i] != s2[i]:
        diff2 += 1

print(min(diff1, diff2))
