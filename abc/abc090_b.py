A, B = map(int, input().split())

ans = 0
for i in range(A, B + 1):
    str_i = str(i)
    if str_i[0] == str_i[-1] and str_i[1] == str_i[-2]:
        ans += 1

print(ans)
