N = int(input())

MOD = 10007

d = [[0] * 10 for _ in range(N)]
for i in range(10):
    d[0][i] = 1
for i in range(1, N):
    for j in range(10):
        if j==0:
            d[i][j] = d[i-1][j]
        else:
            for k in range(j+1):
                d[i][j] += d[i-1][k]
print(sum(d[N-1])%MOD)