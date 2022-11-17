import sys
sys.setrecursionlimit(100000)
T = int(input())

def dfs(graph, vertex, visited):
    if visited[vertex] != True:
        visited[vertex] = True
        for v in graph[vertex]:
            dfs(graph, v, visited)
        return True
    else:
        return False

results = []
for _ in range(T):
    V = int(input())
    e_idx = 1
    graph = [[] for _ in range(V + 1)]
    edge = list(map(int, input().split()))
    for e1 in edge:
        graph[e_idx].append(e1)
        e_idx += 1
    
    visited = [False] * (V + 1)
    result = 0
    for v in range(1, V+1):
        if dfs(graph, v, visited):
            result += 1
    results.append(result)

for r in results:
    print(r)
    