def solve(A, B):
    for i in range(1001):
        if int(i * 0.08) == A and int(i * 0.10) == B:
            return i

    return -1


A, B = map(int, input().split())
print(solve(A, B))
