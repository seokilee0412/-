import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
queue = deque()
for idx in range(M):
    for c_idx in range(N):
        if matrix[idx][c_idx] == 1:
            queue.append([idx,c_idx, 0])
dx = [0,0,1,-1]
dy = [1,-1,0,0]
count = 0
while queue:
    idx, c_idx,counts = queue.popleft()
    
    for i in range(4):
        mx = idx + dx[i]    
        my = c_idx + dy[i]
        if 0<= mx <= M-1 and 0 <= my <= N-1:
            if matrix[mx][my] == 0:
                matrix[mx][my] = 1
                queue.append([mx, my, counts+1])
                count = max(count, counts+1)

for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit()

print(count)