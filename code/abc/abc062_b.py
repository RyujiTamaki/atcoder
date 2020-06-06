H, W = map(int, input().split())
a = [None] * H

for i in range(H):
    a[i] = input()

for i in range(H + 2):
    if i == 0 or i == H + 1:
        out = "#" * (W + 2)
    else:
        out = "#" + a[i - 1] + "#"
    print(out)
