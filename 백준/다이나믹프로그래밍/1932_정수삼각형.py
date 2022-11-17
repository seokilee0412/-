import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

d = deepcopy(triangle)

for i in range(len(d)):
    if i == 0:
        continue
    else:
        for j in range(len(d[i])):
            if j == 0:
                d[i][j] = d[i-1][j] + triangle[i][j]
            elif j == len(d[i]) - 1:
                d[i][j] = d[i-1][j-1] + triangle[i][j]
            else:
                d[i][j] = max(d[i-1][j-1] + triangle[i][j], d[i-1][j] + triangle[i][j])
                
print(max(d[N-1]))