import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
dist = [[0] * (M) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


from collections import deque
def bfs(x, y, graph):
    queue = deque([[x,y]])

    while queue:
        vertex = queue.popleft()
        if vertex[0] == N-1 and vertex[1] == M-1:
            return dist[N-1][M-1]
        else:
            x = vertex[0]
            y = vertex[1]
            if graph[x][y] ==1:
                graph[x][y] = 0
                for i in range(4):
                    mx = x + dx[i]
                    my = y + dy[i]
                    if mx>=0 and mx <= N-1 and my >=0 and my<=M-1:
                        dist[mx][my] = dist[x][y] + 1
                        queue.append([mx, my])
bfs(0,0, graph)
print(dist[N-1][M-1] + 1)

# def dfs(x,y, graph):
#     if graph[x][y] == 1 and x == N-1 and y == M-1:
#         return True
#     if graph[x][y] == 1:
#         # graph[x][y] = 0
#         for i in range(4):
#             mx = x + dx[i]
#             my = y + dy[i]
#             if mx>=0 and mx <= N-1 and my >= 0 and my <= M-1:
#                 if dist[mx][my] > dist[x][y] + 1:
#                     dist[mx][my] = dist[x][y] + 1
#                     dfs(mx,my, graph)
#                 else:
#                     dist[mx][my] = dist[x][y] + 1
#                     dfs(mx,my, graph)
#     else: