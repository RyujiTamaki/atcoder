from itertools import accumulate


def main():
    N = int(input())
    A = list(map(int, input().split()))
    Acum = [0] + A
    Acum = list(accumulate(Acum))

    ans = 0
    for i in range(1, N + 1):
        for j in range(N + 1 - i):
            ans = max(Acum[i + j] - Acum[j], ans)
        print(ans)


if __name__ == "__main__":
    main()
