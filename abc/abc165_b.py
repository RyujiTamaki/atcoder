X = int(input())

m = 100
num = 0
while True:
    if m >= X:
        print(num)
        break
    m += int(m * 0.01)
    num += 1
