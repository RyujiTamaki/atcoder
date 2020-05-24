N = int(input())
S = [None] * N

for i in range(N):
    inp = input()
    S[i] = [s for s in inp]

for i in range(N - 1, -1, -1):
    for j in range(0, 2 * N - 2):
        if S[i][j] == "#":
            try:
                if S[i+1][j-1] == "X":
                    S[i][j] = "X"
            except IndexError:
                continue
            try:
                if S[i+1][j] == "X":
                    S[i][j] = "X"
            except IndexError:
                continue
            try:
                if S[i+1][j+1] == "X":
                    S[i][j] = "X"
            except IndexError:
                continue

for i in range(N):
    print("".join(S[i]))
