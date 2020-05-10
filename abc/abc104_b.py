S = input()
ans = "AC"

if S[0] != "A":
    ans = "WA"

cnt = 0

for i in range(1, len(S)):
    s = S[i]
    if s.isupper():
        if i == 1 or i == len(S) - 1 or s != "C":
            ans = "WA"
        cnt += 1

if cnt != 1:
    ans = "WA"

print(ans)
