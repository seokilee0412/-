from collections import deque
F, S, G, U, D = map(int, input().split())
visited = [False] * F
dist = [0] * F
d = [U, -D]
def bfs(vertex):
    queue = deque([[vertex, 0]])
    visited[vertex] = True
    while queue:
        vertex = queue.popleft()
        place, dist = vertex[0], vertex[1]
        if place == G-1:
            return dist
        for i in range(2):
            new_place = place + d[i]
            if 0<=new_place<=F-1 and visited[new_place] == False:
                visited[new_place] = True
                queue.append([new_place, dist + 1])
    return 'use the stairs'

print(bfs(S-1))