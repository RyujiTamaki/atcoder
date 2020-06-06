A, B = map(int, input().split())
S = input()

s = S.split("-")

ans = "Yes" if (A == len(s[0]) and B == len(s[1])) else "No"
print(ans)
