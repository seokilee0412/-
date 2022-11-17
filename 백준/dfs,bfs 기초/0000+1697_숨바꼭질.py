N, K = map(int, input().split())
from collections import deque

def bfs():
    queue = deque([N])

    while queue:
        x = queue.popleft()
        if x == K:
            return dist[x]

        for nx in (x-1, x+1, 2*x):
            if 0<= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)
            
MAX = 10**5
dist = [0 for _ in range(MAX + 1)]
print(bfs())
