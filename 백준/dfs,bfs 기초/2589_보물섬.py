from collections import deque
import sys
X,Y = map(int, sys.stdin.readline().split())

graph = [sys.stdin.readline().rstrip() for _ in range(X)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y, graph):
    visited = [[0] * Y for _ in range(X)]
    queue = deque([[x, y, 0]])
    max_dist = -1
    while queue:
        vertex = queue.popleft()
        x, y, dist = vertex
        visited[x][y] = 1
        if dist > max_dist:
            max_dist = dist
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx >=0 and mx <=X-1 and my >=0 and my<=Y-1 and graph[mx][my] == 'L' and visited[mx][my] == 0:
                queue.append([mx, my, dist + 1])
    return max_dist

max_dists = -1e10
for i in range(X):
    for j in range(Y):
        if graph[i][j] == 'L':
            dists = bfs(i,j, graph)
            max_dists = max(max_dists, dists)

print(max_dists)


from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i, j):
    q = deque()
    q.append([i, j])
    max_n = 0
    while q:
        a, b = q.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0 and s[x][y] != "W":
                visit[x][y] = 1
                s[x][y] = s[a][b] + 1
                max_n = max(max_n, s[x][y])
                q.append([x, y])
    return max_n
n, m = map(int, input().split())
s = []
result = 0
for i in range(n):
    s.append(list(input().strip()))
for i in range(n):
    for j in range(m):
        if s[i][j] != "W":
            visit = [[0] * m for _ in range(n)]
            s[i][j] = 0
            visit[i][j] = 1
            result = max(result, bfs(i, j))
print(result)