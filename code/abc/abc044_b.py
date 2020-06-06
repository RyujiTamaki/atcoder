from collections import Counter

w = input()
c = Counter(w)

ans = "Yes"

for v in c.values():
    if v % 2 == 1:
        ans = "No"

print(ans)
