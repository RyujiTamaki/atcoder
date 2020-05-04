def solve(W):
    set_W = set(W)
    if len(W) != len(set_W):
        return False

    for i in range(len(W) - 1):
        if W[i][-1] != W[i + 1][0]:
            return False

    return True


N = int(input())
W = [input() for _ in range(N)]

if solve(W):
    print("Yes")
else:
    print("No")
