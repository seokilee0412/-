T = int(input())
import sys
sys.setrecursionlimit(100000000)
results = []
def dfs(x, y, matrix):
    if matrix[y][x] == 1:
        matrix[y][x] == 0
        if x > 0:
            dfs(x-1, y, matrix)
        if y < N:
            dfs(x, y+1, matrix)
        if x < M:
            dfs(x+1, y, matrix)
        if y > 0:
            dfs(x, y-1, matrix)
        return True
    else:
        return False

for _ in range(T):
    M, N, K = map(int, input().split())

    x, y = 0, 0
    matrix = [[0] * (M) for _ in range(N)]

    for e in range(K):
        e1, e2 = map(int, input().split())
        matrix[e2][e1] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j, matrix):
                result += 1
    results.append(result)

for r in results:
    print(r)
print('done')