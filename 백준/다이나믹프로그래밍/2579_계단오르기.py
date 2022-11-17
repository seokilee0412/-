import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]
if len(numbers) == 1:
    print(numbers[0])
elif len(numbers) == 2:
    print(numbers[0] + numbers[1])
elif len(numbers) == 3:
    first = numbers[0] + numbers[2]
    second = numbers[1] + numbers[2]
    print(max(first, second))
else:
    d = [[0] * 2 for i in range(N)] # d[i][0] : 자신의 앞앞 밟은 것, d[i][1] : 자신 바로 앞 밟은 것
    d[0][0] = numbers[0]
    d[0][1] = numbers[0]

    d[1][0] = numbers[1]
    d[1][1] = numbers[1] + numbers[0]

    for i in range(2, len(numbers)):
        if i == len(numbers) - 1:
            d[i][0] = d[i-1][0] + numbers[i]
            d[i][1] = max(d[i-2]) + numbers[i]
            print(max(d[i]))
        else:
            d[i][0] = max(d[i- 2]) + numbers[i]
            d[i][1] = d[i-1][0] + numbers[i]

