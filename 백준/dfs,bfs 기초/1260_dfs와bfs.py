N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    v,e = map(int, input().split())
    graph[v][e] = graph[e][v] = 1

visited = [False] * (N + 1)

def dfs(vertex, visited, graph):
    visited[vertex] = True
    print(vertex, end=' ')
    for v in range(len(graph[vertex])):
        if visited[v] == False and graph[vertex][v] == 1:
            dfs(v, visited, graph)

dfs(V, visited, graph)

print()
visited = [False] * (N + 1)

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(len(graph[v])):
            if not visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True
bfs(graph, V, visited)
