# using heap
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
problem_count = 1
while True:
    N = int(input())
    if N == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(N)]
    costs = [[10000000] * N for _ in range(N)]
    heap = []
    heappush(heap, [0,0, matrix[0][0]])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while heap:
        x, y, cost = heappop(heap)

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if 0<=mx<=N-1 and 0<=my<=N-1:
                new_cost = cost + matrix[mx][my]
                if new_cost < costs[mx][my]:
                    costs[mx][my] = new_cost
                    heappush(heap, [mx, my, new_cost])

    print(f'Problem {problem_count}: {costs[-1][-1]}')
    problem_count += 1