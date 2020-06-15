X, Y = map(int, input().split())

if Y % 2 == 1:
    print("No")
    exit()

max_y = 4 * X
min_y = 2 * X

if max_y >= Y >= min_y:
    print("Yes")
else:
    print("No")
