from collections import deque
n = int(input())
m = int(input())

graph =[[] for _ in range(n + 1)]
vistied = [False] * (n+1)

for e in range(m):
    e1, e2 = map(int, input().split())
    graph[e1].append(e2)
    graph[e2].append(e1)

dist = [0 for _ in range(n+1)]
def bfs(start, graph, visited):
    queue =deque([start])

    while queue:
        vertex = queue.popleft()
        visited[vertex] = True
        if dist[vertex] > 2:
            break
        for v in graph[vertex]:
            if vistied[v] != True and v not in queue:
                dist[v] = dist[vertex] + 1
                queue.append(v)
    return dist
distance = bfs(1, graph, vistied)
idx = 0
count = 0
for d in distance:
    if 0 < d <=2:
        count += 1    
    idx += 1
print(count)