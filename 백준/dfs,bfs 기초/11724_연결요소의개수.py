N, M = map(int, input().split())
import sys
graph = [[] for _ in range(N+1)]

sys.setrecursionlimit(10000)

for _ in range(M):

    e1, e2 = map(int,sys.stdin.readline().split())
    graph[e1].append(e2)
    graph[e2].append(e1)

visited = [False] * (N+1)


def dfs(graph, vertex, visited):
    if visited[vertex] == False:
        visited[vertex] = True
        for v in graph[vertex]:
            if visited[v] != True:
                dfs(graph, v, visited)
        return True
    return False

result = 0
for v in range(1, N+1):
    if dfs(graph, v, visited):
        result += 1

print(result)