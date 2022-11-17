import sys
from collections import deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N, L, R = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
dx = [1,-1, 0,0]
dy = [0,0, -1,1]
def bfs(x,y, visited):
    queue = deque([[x,y,matrix[x][y]]])
    
    change_country = [[x, y]]
    country_count = 1
    total_population = matrix[x][y]
    while queue:
        vertex = queue.popleft()
        x, y, population = vertex[0], vertex[1], vertex[2]
        
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx>=0 and my>=0 and mx<=N-1 and my<=N-1 and visited[mx][my] == False:
                if L<= abs(population - matrix[mx][my]) <= R:
                    visited[mx][my] = True
                    queue.append([mx, my, matrix[mx][my]])
                    total_population += matrix[mx][my]
                    country_count += 1
                    change_country.append([mx, my])
    if country_count > 1:
        for n_x, n_y in change_country:
            matrix[n_x][n_y] = int(total_population/country_count)
        return True
    else:
        return False

stop = True
day_count = 0
while stop:
    
    visited = [[False] * N for _ in range(N)]
    stop = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                visited[i][j] = True
                if bfs(i, j, visited):
                    
                    stop = True
    if stop == True:
        day_count += 1
    else:
        break

print(day_count)
    
        