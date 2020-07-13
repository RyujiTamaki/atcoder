import math
from itertools import permutations


N = int(input())
point = [None] * N
for i in range(N):
    x, y = map(int, input().split())
    point[i] = (x, y)

total_distance = 0
num = 0
for perm_points in permutations(point, N):
    num += 1
    for i in range(N - 1):
        p1 = perm_points[i]
        p2 = perm_points[i + 1]
        total_distance += math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

print(total_distance / num)
