A, B, K = map(int, input().split())

divisor = []

for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        divisor.append(i)

print(divisor[-K])
