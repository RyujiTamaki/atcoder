N = int(input())
prev_t, prev_x, prev_y = 0, 0, 0
can = True

for _ in range(N):
    t, x, y = map(int, input().split())
    dt = t - prev_t
    dist = abs(x - prev_x) + abs(y - prev_y)
    if dt < dist or dist % 2 != dt % 2:
        can = False
    prev_t = t
    prev_x = x
    prev_y = y

if can:
    print("Yes")
else:
    print("No")
