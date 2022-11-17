import sys
sys.setrecursionlimit(10000)
N = int(input())
graph = [input() for _ in range(N)]

normal = {'R' : 2, 'B' : 1, 'G' : 0}
not_normal = {'R' : 1, 'B' : 0, 'G' : 1}

normal_graph = []
not_normal_graph = []
for gs in graph:
    sub_gr_norm = []
    sub_gr_not_norm = []
    for g in gs:
        sub_gr_norm.append(normal[g])
        sub_gr_not_norm.append(not_normal[g])
    normal_graph.append(sub_gr_norm)
    not_normal_graph.append(sub_gr_not_norm)

dx = [1,-1, 0,0]
dy = [0,0, 1, -1]

def dfs(x, y, color, graph):
    if graph[x][y] == color:
        graph[x][y] = -1
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx >=0 and mx <=N-1 and my >=0 and my<= len(graph[0]) -1:
                dfs(mx,my,color,graph)
        return True
    else:
        False

#normal
seg = 0
for i in range(N):
    for j in range(len(graph[0])):
        if dfs(i,j,0,normal_graph):
            seg += 1
        elif dfs(i,j,1,normal_graph):
            seg += 1
        elif dfs(i,j,2,normal_graph):
            seg += 1
seg_not_normal = 0
for i in range(N):
    for j in range(len(graph[0])):
        if dfs(i,j,0,not_normal_graph):
            seg_not_normal += 1
        elif dfs(i,j,1,not_normal_graph):
            seg_not_normal += 1

print(seg)
print(seg_not_normal)