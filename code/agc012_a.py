N = int(input())
a = list(map(int, input().split()))
a.sort()
x = sum(a[N::2])
print(x)
