import sys
from copy import deepcopy

input = sys.stdin.readline

T = int(input())
result = []
for i in range(T):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(2)]
    d = deepcopy(numbers)
    if N == 1:
        result.append(max(numbers[0][0], numbers[1][0]))
    else:
        d[0][1] = d[1][0] + numbers[0][1]
        d[1][1] = d[0][0] + numbers[1][1]

        for i in range(2, N):
            d[0][i] = numbers[0][i] + max( d[1][i-1], d[0][i-2], d[1][i-2] )
            d[1][i] = numbers[1][i] + max( d[0][i-1], d[0][i-2], d[1][i-2] )

        result.append(max(max(d[0]),max(d[1])))

for r in result:
    print(r)