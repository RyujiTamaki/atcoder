import string

N = int(input())
alphabet = list(string.ascii_lowercase)
num2alphabet = {i + 1: a for i, a in enumerate(alphabet)}
num2alphabet[0] = "z"
ans = ""

while N > 0:
    num = N % 26
    ans += num2alphabet[num]
    if N <= 26:
        break

    if num == 0:
        N -= 1

    N = N // 26

print(''.join(list(reversed(ans))))
