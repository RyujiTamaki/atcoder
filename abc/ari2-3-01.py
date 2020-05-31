# i番目以降の品物から重さの総和がj以下となるように選ぶ
def rec(i: int, j: int) -> int:
    if i == n:
        # もう品物は残っていない
        res = 0
    elif j < w[i]:
        # この品物は入らない
        res = rec(i + 1, j)
    else:
        # 入れない場合と入れる場合を両方試す
        res = max(rec(i + 1, j), rec(i + 1, j - w[i]) + v[i])

    return res


n  = int(input())
w = []
v = []
for i in range(n):
    w_, v_ = map(int, input().split())
    w.append(w_)
    v.append(v_)
W = int(input())

print(rec(0, W))
