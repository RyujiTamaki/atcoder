import sys
from bisect import bisect_left


def solve():
    input = sys.stdin.readline
    N = int(input())
    R = [[int(i) for i in input().split()] for _ in range(N)]

    # レートのみの配列を作り、ソートする
    rates = [R[i][0] for i in range(N)]
    rates.sort()

    # 各ランク毎のグー、チョキ、パーの数
    hands = [[0, 0, 0] for _ in range(100001)]
    for i in range(N):
        hands[R[i][0]][R[i][1] - 1] += 1

    ans = [[] for _ in range(N)]
    for i in range(N):
        rate, hand = R[i]

        # bisect_left(rates, rate)
        win = bisect_left(rates, rate) + hands[rate][hand % 3]

        # 同じレートで同じ手
        draw = hands[rate][hand - 1] - 1
        lose = (N - 1) - win - draw
        ans[i] = [win, lose, draw]

    for i in range(N):
        print(*ans[i], sep=" ")


if __name__ == "__main__":
    solve()
