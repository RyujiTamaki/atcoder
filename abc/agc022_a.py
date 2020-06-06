from string import ascii_lowercase
S = input()

if S == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()

if len(S) < 26:
    for a in ascii_lowercase:
        if a not in set(list(S)):
            print(S + a)
            exit()

T = S
S = "".join(sorted(S))
ans= ""
for i in range(26):
    if S[i] > T[i]:
        break
    ans += S[i]

print(ans)
