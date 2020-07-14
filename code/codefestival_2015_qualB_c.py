N, M = map(int, input().split())
A = list(map(int, input().split()))  # 部屋の定員
B = list(map(int, input().split()))  # 予約の人数

A.sort(reverse=True)
B.sort(reverse=True)

can = False
if N >= M:
    can = True
    for a, b in zip(A, B):
        if a < b:
            can = False

if can:
    print("YES")
else:
    print("NO")
