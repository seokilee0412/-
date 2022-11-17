import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
max_range = 1e-10
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        max_range = max(max_range, matrix[i][j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, num):
    if visited[x][y] == False:
        visited[x][y] = True
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if 0<=mx<=N-1 and 0<=my<=N-1 and visited[mx][my] == False and matrix[mx][my] > num:
                dfs(mx, my, num)
        return True
    else:
        return False

max_value = 1e-10
for num in range(max_range + 1):
    count = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False and matrix[i][j] > num:
                if dfs(i, j, num):
                    count +=1 
    max_value = max(max_value, count)

print(max_value)