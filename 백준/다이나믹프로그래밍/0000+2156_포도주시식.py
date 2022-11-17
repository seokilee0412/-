import sys
input = sys.stdin.readline

N = int(input())

numbers = [int(input()) for _ in range(N)]

d = [[i, i] for i in numbers]

if N == 1:
    print(numbers[0])
else:
    d[1][0] = d[0][1] + d[1][0]
    d[1][1] =  d[1][1]

    maximum = d[1][0]

    for i in range(2, N):
        d[i][0] = d[i-1][1] + numbers[i]
        d[i][1] = numbers[i] + max(d[i-2][0], d[i-2][1])
        if d[i][0] > maximum:
            maximum = d[i][0]
        if d[i][1] > maximum:
            maximum = d[i][1]

    print(maximum)