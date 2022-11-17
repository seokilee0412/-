S = int(input())
check = set()
num = 1
for n in range(100000):
    if S == 1:
        result = 1
        break
    else:
        sum_n = (n * (n + 1)) / 2
        if S - sum_n < 0:
            result = n - 1
            break

print(result)

