s = input()

a = len(s) + 1
z = -1

for i in range(len(s)):
    if s[i] == "A":
        a = min(a, i)
    if s[i] == "Z":
        z = max(z, i)

print(len(s[a:z+1]))
