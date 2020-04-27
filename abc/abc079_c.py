import sys


def dfs(i, s, val, formula):
    if (i == len(s) - 1):
        if val == 7:
            print(formula + "=7")
            sys.exit()
            return formula
        else:
            return None

    dfs(i + 1, s, val + int(s[i + 1]), formula + "+" + s[i + 1])
    dfs(i + 1, s, val - int(s[i + 1]), formula + "-" + s[i + 1])
    return None


s = input()
dfs(0, s, int(s[0]), s[0])
