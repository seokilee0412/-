import sys

computer = int(input())
E = int(input())
graph = [[] for _ in range(computer+1)]

for _ in range(E):
    e1, e2 = map(int, sys.stdin.readline().rstrip().split())
    graph[e1].append(e2)
    graph[e2].append(e1)

visited = [False] * (computer + 1)
count = 0
def dfs(vertex, graph, visited):
    if visited[vertex] == False:
        visited[vertex] = True
        for v in graph[vertex]:
            if visited[v] != True:
                dfs(v, graph, visited)
        return True
    else:
        return False

dfs(1, graph, visited)
print(sum(visited) - 1)