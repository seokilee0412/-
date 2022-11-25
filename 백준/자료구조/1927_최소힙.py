import sys
import heapq
input = sys.stdin.readline
N = int(input())

command = [int(input()) for _ in range(N)]
result = []
heap = []
for c in command:
    if c == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, c)

for r in result:
    print(r)