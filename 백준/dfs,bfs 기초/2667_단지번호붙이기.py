import sys
sys.setrecursionlimit(1000000)
N = int(input())
dx = [-1,1, 0, 0]
dy = [0, 0, -1, 1]
matrix = [list(map(int, input())) for _ in range(N)]
HOUSE_COUNT = 0 
def dfs(x, y, matrix):

    if matrix[x][y] == 1:
        global HOUSE_COUNT
        HOUSE_COUNT += 1
        matrix[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >=0 and ny<N:
                dfs(nx, ny, matrix)
        return True
    else:
        return False
danji = 0
house = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            if dfs(i, j, matrix):
                danji += 1
                house.append(HOUSE_COUNT)
                HOUSE_COUNT = 0
            
print(danji)
house.sort()
for h in house:
    print(h)