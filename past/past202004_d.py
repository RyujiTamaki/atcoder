def n_gram(target, n):
  return [target[idx:idx + n] for idx in range(len(target) - n + 1)]


S = input()
T = []
for i in range(1, len(S) + 1):
    T.extend(n_gram(S, i))

T = set(T)
ans = []

for t in T:
    if len(t) == 1:
        ans.append(".")
    else:
        for i in range(len(t)):
            tmp = t
            tmp[i] = "."
            ans.append(tmp)
print(set(ans))

