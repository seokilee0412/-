import sys
import heapq

input = sys.stdin.readline

N = int(input())
command = [int(input()) for _ in range(N)]
heap = []
for c in command:
    if c == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(c), c))