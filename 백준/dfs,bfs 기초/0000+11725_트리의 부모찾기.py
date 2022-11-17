N = int(input())
import sys
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    e1, e2 = map(int, sys.stdin.readline().rstrip().split())
    graph[e1].append(e2)
    graph[e2].append(e1)

visited = [False] * (N+1)

# for v in graph:
#     if len(v) == 1:
#         print(v)
#     elif len(v) >