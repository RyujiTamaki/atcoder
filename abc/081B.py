import math
n = input()
a = list(map(int, input().split()))
ans = 10 ** 9

for i in a:
    count = 0

    while i % 2 == 0:
        i /= 2
        count += 1

    ans = min(ans, count)

print(ans)
