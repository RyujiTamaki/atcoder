import collections

S = input()
S = [s for s in S]

c = collections.Counter(S)
print(max(c, key=c.get))
