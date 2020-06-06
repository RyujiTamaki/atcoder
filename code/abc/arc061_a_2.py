def cal(formula: str) -> int:
    nums = formula.split("+")
    ans = 0
    for n in nums:
        ans += int(n)
    return ans


def dfs(i: int, s: str, formula: str) -> int:
    # 終端条件
    if i == len(s) - 1:
        return cal(formula)

    return dfs(i + 1, s, formula + s[i + 1]) + dfs(i + 1, s, formula + "+" + s[i + 1])


S = input()
print(dfs(0, S, S[0]))
