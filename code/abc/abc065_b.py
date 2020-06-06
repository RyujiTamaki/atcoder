N = int(input())
a = [int(input()) - 1 for i in range(N)]
c, s = 1, a[0]

while s != 2 and c < N:
    c = c + 1
    s = a[s - 1]

now = 0
c = 0

while True:
    if now == 1:
        print(c)
        break
    if c >= N:
        print("-1")
        break
    c += 1
    now = a[now]
