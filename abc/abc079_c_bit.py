s = input()

for i in range(2**(len(s)-1)):
    formula = s[0]
    val = int(s[0])
    for j in range(len(s)-1):
        if ((i>>j) & 1):
            formula += "+" + s[j+1]
            val += int(s[j+1])
        else:
            formula += "+" + s[j+1]
            val -= int(s[j+1])
    if val == 7:
        print(formula + "=7")
        break
