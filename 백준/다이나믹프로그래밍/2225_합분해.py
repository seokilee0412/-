import sys
input = sys.stdin.readline
N, K = map(int, input().split())

d = [[0] * 200 for _ in range(200)]
for i in range(N):
    d[0][i] = 1
    d[1][i] = i+2
for i in range(K):
    d[i][0] = i+1
for i in range(2, K):
    for j in range(N):
        if d[i][j] == 0:
            d[i][j] = d[i-1][j] + d[i][j-1]

print(d[K-1][N-1] % 1000000000)