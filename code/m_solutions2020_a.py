X = int(input())

for i in range(8):
    low = i * 200 + 400
    high = low + 200
    if low <= X < high:
        print(8 - i)

