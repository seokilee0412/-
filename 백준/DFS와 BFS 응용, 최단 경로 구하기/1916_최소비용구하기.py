import sys
from collections import defaultdict, deque
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())


s = [[] for i in range(N + 1)]
for i in range(M):
    a, b, w = map(int, input().split())
    s[a].append([b, w])
start, end = map(int, input().split())

#dfs
path = defaultdict(dict)

for _ in range(M):
    s, e, c = map(int, input().split())

    path[s][e] = c
def dfs(s, cost):
    if s == end:
        return cost
    
    else:
        list_end = list(path[s].keys())
        costs = 10000
        for e in list_end:
            costs = min(costs, dfs(e, cost + path[s][e]))
        return costs
cc = 100000
for p in path[start].keys():
    cc = min(cc, dfs(p, path[start][p]))
print(cc)

###queue
inf = 100000000
dp = [inf for i in range(N + 1)]
# queue = deque([[start, 0]])
# dp[start] = 0
# queue = []
# heapq.heappush(queue, [0, start])
def dijkstra(start):
    dp[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    while queue:
        # end, cost = queue.popleft()
        cost, end = heapq.heappop(queue)
        if dp[end] < cost:
            continue
        # for p in path[end].keys():
        for p, n_c in s[end]:
            new_end = p
            # new_cost = cost + path[end][p]
            new_cost = cost + n_c
            if dp[new_end] > new_cost:
                dp[new_end] = new_cost
                # queue.append([new_end, new_cost])
                heapq.heappush(queue, [new_cost, new_end])
dijkstra(start)
print(dp[end])