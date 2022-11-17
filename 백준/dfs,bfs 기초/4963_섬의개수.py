import sys
sys.setrecursionlimit(10000)

nh = [-1, 1 , 0, 0, 1, 1, -1 , -1]
nw = [0, 0, 1, -1, 1, -1, 1, -1] 

def dfs(h, w, matrix):
    if matrix[h][w] == 1:
        matrix[h][w] = 0
        for i in range(8):
            mh = h + nh[i]
            mw = w + nw[i]
            if mh >=0 and mh <H and mw >=0 and mw<W:
                dfs(mh, mw, matrix)
        return True
    else:
        return False
counts = []
while True:

    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(H)]
    count = 0
    for i in range(W):
        for j in range(H):
            if matrix[j][i] == 1:
                if dfs(j, i, matrix):
                    count += 1
    counts.append(count)

for c in counts:
    print(c)   
