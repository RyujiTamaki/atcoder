import math

A, B, H, M = map(int, input().split())

A_degree = H * 30 + 0.5 * M
B_degree = M * 6

AB = math.sqrt(A * A + B * B - 2 * A * B * math.cos(math.radians(A_degree - B_degree)))
print(AB)
