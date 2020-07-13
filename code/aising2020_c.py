N = int(input())
ans = [0 for _ in range(10050)]

for x in range(1, 105):
    for y in range(1, 105):
        for z in range(1, 105):
            v = x * x + y * y + z * z + x * y + y * z + z * x
            if v < 10050:
                ans[v] += 1

for i in range(N):
    print(ans[i + 1])
