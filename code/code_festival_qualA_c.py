A, B = map(int, input().split())

"""
O(N)解法
ans = 0
for i in range(A, B + 1):
    if i % 400 == 0:
        ans += 1
    elif i % 100 == 0:
        continue
    elif i % 4 == 0:
        ans += 1

print(ans)
"""

# O(1)解法
A = A - 1
num_4 = B // 4 - A // 4
num_100 = B // 100 - A // 100
num_400 = B // 400 - A // 400

print(num_4 - num_100 + num_400)
