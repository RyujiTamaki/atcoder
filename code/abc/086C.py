n = int(input())
t_, x_, y_ = 0, 0, 0
for i in range(n):
    t, x, y = map(int, input().split())
    dt = t - t_
    dist = abs(x - x_) + abs(y - y_)
    if dt < dist or (dist % 2 != dt % 2):
        print("No")
        exit()
    t_, x_, y_ = t, x, y

print("Yes")
