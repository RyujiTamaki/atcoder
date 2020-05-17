S = input()

for i in range(1, len(S)):
    s = S[:-i]
    if len(s) % 2 != 0:
        continue

    half_length = int(len(s) / 2)
    if s[:half_length] == s[half_length:]:
        print(len(s))
        break
