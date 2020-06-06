O = input()
E = input()

ans = ""
O = [o for o in O]
E = [e for e in E]

for i in range(len(O) + len(E)):
    if i % 2 == 0:
        ans += O.pop(0)
    else:
        ans += E.pop(0)

print(ans)
